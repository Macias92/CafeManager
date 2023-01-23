from django.urls.conf import include, path
from django.urls import re_path
from rest_framework.routers import DefaultRouter
from .viewsets import PurchaseViewSet
from purchase.views import PurchaseListView, CancellingPurchaseView

router = DefaultRouter()

router.register(
    r'purchase',
    PurchaseViewSet,
    basename="purchase"
)

urlpatterns = [
    re_path(r'', include(router.urls)),
    path('purchase-list/', PurchaseListView.as_view(), name="purchase_list"),
    path('purchase-cancel/<int:pk>/', CancellingPurchaseView.as_view(),
         name="purchase_cancel"),
]
