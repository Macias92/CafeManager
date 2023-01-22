from rest_framework.viewsets import ModelViewSet
from authx.permissions import IsCashierUser
from .serializers import (
    CreatePurchaseOrderSerializer,
    PurchaseOrderSeralizer
)
from .models import PurchaseOrder


class PurchaseViewSet(ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    permission_classes = [IsCashierUser]
    
    def get_serializer_class(self):
        if self.action in ['update', 'partial_update', 'create']:
            return CreatePurchaseOrderSerializer
        else:
            return PurchaseOrderSeralizer