from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    VendorViewSet,
    PurchaseOrderViewSet,
    PurchaseOrderAcknowledgmentView,
    HistoricalPerformanceViewSet,
    VendorPerformanceView,
)

router = DefaultRouter()
router.register(r'vendors', VendorViewSet, basename='vendor')
router.register(r'purchase_orders', PurchaseOrderViewSet, basename='purchase_order')
router.register(r'historical_performance', HistoricalPerformanceViewSet, basename='historical_performance')

urlpatterns = [
    path('', include(router.urls)),
    path('purchase_orders/<int:po_id>/acknowledge/', PurchaseOrderAcknowledgmentView.as_view(), name='purchase-order-acknowledge'),
    path('vendors/<int:vendor_id>/performance/', VendorPerformanceView.as_view(), name='vendor-performance'),
]
