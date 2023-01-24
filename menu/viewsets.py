from rest_framework.viewsets import ModelViewSet
from authx.permissions import MenuViewPermission
from .serializers import (
    MenuSerializer,
    CashierMenuSerializer,
    AdminMenuSerializer,
    MenuItemSerializer,
    CashierMenuItemSerializer,
    ManagerMenuItemSerializer,
    ComponentSerializer,
    ManagerComponentSerializer,
    CreateMenuItemSerializer,
    CreateMenuSerializer,

)
from .models import Menu, MenuItem, Component


class MenuViewSet(ModelViewSet):
    """ViewSet for Menu object"""
    queryset = Menu.objects.all()
    permission_classes = [MenuViewPermission]

    def get_serializer_class(self):
        if self.request.user.role == 1:
            return CashierMenuSerializer
        elif self.request.user.role >= 3:
            if self.action in ['update', 'partial_update', 'create']:
                return CreateMenuSerializer
            return AdminMenuSerializer
        else:
            if self.action in ['update', 'partial_update', 'create']:
                return CreateMenuSerializer
            return MenuSerializer


class MenuItemViewSet(ModelViewSet):
    """ViewSet for items of the menu object"""
    queryset = MenuItem.objects.all()
    permission_classes = [MenuViewPermission]

    def get_serializer_class(self):
        if self.request.user.role == 1:
            return CashierMenuItemSerializer
        elif self.request.user.role >= 3:
            if self.action in ['update', 'partial_update', 'create']:
                return CreateMenuItemSerializer
            return ManagerMenuItemSerializer
        else:
            if self.action in ['update', 'partial_update', 'create']:
                return CreateMenuItemSerializer
            return MenuItemSerializer


class ComponentViewSet(ModelViewSet):
    """ViewSet for Component object"""
    queryset = Component.objects.all()
    permission_classes = [MenuViewPermission]

    def get_serializer_class(self):
        if self.request.user.role >= 3:
            return ManagerComponentSerializer
        else:
            return ComponentSerializer
