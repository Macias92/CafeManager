from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from .models import PurchaseOrder
from .serializers import ListPurchaseOrderSerializer


class PurchaseListView(ListAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = ListPurchaseOrderSerializer
    permission_classes = [AllowAny]