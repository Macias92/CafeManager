from datetime import datetime
from menu.serializers import CashierMenuItemSerializer
from rest_framework.serializers import (
    ModelSerializer,
    PrimaryKeyRelatedField,
    CharField,
    ValidationError
)
from django.utils.translation import gettext_lazy as _
from .models import PurchaseOrder
from menu.models import MenuItem, Component


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
    def to_internal_value(self, data):
        today = datetime.now()
        count_today = PurchaseOrder.objects.filter(
            created_date__date=today).count()+1
        data['order_number'] = f"{today.strftime('%d%m%y')}_{count_today}"

        return super(CreatePurchaseOrderSerializer, self).to_internal_value(data)

    items = PrimaryKeyRelatedField(many=True, queryset=MenuItem.objects.all())

    def validate(self, data):
        all_quantity = {}
        for item in data['items']:
            for component in item.ingredients.all():
                if component.pk in all_quantity:
                    all_quantity[component.pk] += component.quantity
                else:
                    all_quantity[component.pk] = component.quantity

        for key in all_quantity.keys():
            new_obj = Component.objects.get(pk=key).ingredient
            all_res = all_quantity[key]
            if all_res > new_obj.quantity:
                raise ValidationError(_("No ingredients!"))

        return super(CreatePurchaseOrderSerializer, self).validate(data)
