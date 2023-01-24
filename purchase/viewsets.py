from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin
)
from authx.permissions import IsCashierUser
from .serializers import (
    CreatePurchaseOrderSerializer,
    PurchaseOrderSeralizer
)
from .models import PurchaseOrder
from cafemanager.mixins import CustomLoggingViewSetMixin


class PurchaseViewSet(CustomLoggingViewSetMixin,
                      CreateModelMixin,
                      ListModelMixin,
                      RetrieveModelMixin,
                      UpdateModelMixin,
                      GenericViewSet):
    """ViewSet for purchasing, where user can create, retrieve, udpate simple purchase and list all purchases"""
    queryset = PurchaseOrder.objects.all()
    permission_classes = [IsCashierUser]

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update', 'create']:
            return CreatePurchaseOrderSerializer
        else:
            return PurchaseOrderSeralizer
