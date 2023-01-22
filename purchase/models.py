from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from menu.models import MenuItem

User = get_user_model()

class PurchaseOrder(models.Model):
    STATUS_CHOICE = (
        (1, _("New")),
        (2, _("Pending")),
        (3, _("Ready")),
        (4, _("Retrieved")),
    )
    items = models.ManyToManyField(MenuItem)
    status = models.PositiveIntegerField(choices=STATUS_CHOICE, default=1)
    order_number = models.CharField(max_length=64)
    client_name = models.CharField(max_length=64, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return f"{self.order_number} - {self.get_status_display()}"
    