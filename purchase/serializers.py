from menu.serializers import CashierMenuItemSerializer
from rest_framework.serializers import (
    ModelSerializer,
    PrimaryKeyRelatedField,
    CharField
)
from .models import PurchaseOrder
from menu.models import MenuItem


class ListPurchaseOrderSerializer(ModelSerializer):
    status = CharField(source='get_status_display')

    class Meta:
        model = PurchaseOrder
        fields = ["status", "order_number"]


class PurchaseOrderSeralizer(ModelSerializer):
    items = CashierMenuItemSerializer(many=True)

    class Meta:
        model = PurchaseOrder
        felds = "__all__"


class CreatePurchaseOrderSerializer(ModelSerializer):
    items = PrimaryKeyRelatedField(many=True, queryset=MenuItem.objects.all())
