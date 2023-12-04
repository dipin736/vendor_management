# views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.utils import timezone
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from .serializers import VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer
from rest_framework import viewsets

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class HistoricalPerformanceViewSet(viewsets.ModelViewSet):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer

# class VendorListCreateView(generics.ListCreateAPIView):
#     queryset = Vendor.objects.all()
#     serializer_class = VendorSerializer

# class VendorRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Vendor.objects.all()
#     serializer_class = VendorSerializer

class VendorPerformanceView(APIView):
    def get(self, request, vendor_id):
        try:
            vendor = Vendor.objects.get(pk=vendor_id)
            performance_data = {
                'on_time_delivery_rate': vendor.on_time_delivery_rate,
                'quality_rating_avg': vendor.quality_rating_avg,
                'average_response_time': vendor.average_response_time,
                'fulfillment_rate': vendor.fulfillment_rate,
            }
            return Response(performance_data, status=status.HTTP_200_OK)
        except Vendor.DoesNotExist:
            return Response({'detail': 'Vendor not found'}, status=status.HTTP_404_NOT_FOUND)

class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderAcknowledgmentView(APIView):
    def post(self, request, po_id):
        try:
            purchase_order = PurchaseOrder.objects.get(pk=po_id)
            purchase_order.acknowledgment_date = timezone.now()
            purchase_order.save()

            return Response({'detail': 'Acknowledgment successful'}, status=status.HTTP_200_OK)
        except PurchaseOrder.DoesNotExist:
            return Response({'detail': 'Purchase Order not found'}, status=status.HTTP_404_NOT_FOUND)

# class HistoricalPerformanceListCreateView(generics.ListCreateAPIView):
#     queryset = HistoricalPerformance.objects.all()
#     serializer_class = HistoricalPerformanceSerializer

# class HistoricalPerformanceRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = HistoricalPerformance.objects.all()
#     serializer_class = HistoricalPerformanceSerializer
