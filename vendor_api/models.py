# models.py
from django.db import models
from django.db.models import Avg
from django.utils import timezone

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

    def calculate_metrics(self):
        completed_orders = self.purchaseorder_set.filter(status='completed')

        # On-Time Delivery Rate
        on_time_delivery_count = completed_orders.filter(delivery_date__lte=timezone.now()).count()
        self.on_time_delivery_rate = (on_time_delivery_count / completed_orders.count()) * 100 if completed_orders.count() > 0 else 0

        # Quality Rating Average
        self.quality_rating_avg = completed_orders.aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0

        # Average Response Time
        response_times = completed_orders.annotate(response_time=models.F('acknowledgment_date') - models.F('issue_date'))
        avg_response_time = response_times.aggregate(Avg('response_time'))['response_time__avg']

        if avg_response_time is not None:
            self.average_response_time = avg_response_time.total_seconds() / 3600 if avg_response_time.total_seconds() > 0 else 0
        else:
            self.average_response_time = 0

        # Fulfilment Rate
        total_orders = self.purchaseorder_set.all()
        self.fulfillment_rate = (completed_orders.filter(status='completed').count() / total_orders.count()) * 100 if total_orders.count() > 0 else 0

        self.save()


class PurchaseOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', 'pending'),
        ('completed', 'completed'),
        ('canceled', 'canceled'),
    ]
    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.po_number} - {self.vendor.name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.vendor.calculate_metrics()

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"