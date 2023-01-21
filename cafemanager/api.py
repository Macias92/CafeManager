from django.urls.conf import include
from django.urls import path


urlpatterns = [
    path('authx/', include('authx.urls')),
    path('store/', include('store.urls')),
    path('supplier/', include('supplier.urls')),

]
