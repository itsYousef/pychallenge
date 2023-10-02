from django.urls import path
from .views import DeviceDetailApiView, DeviceListApiView

urlpatterns = [
    path('', DeviceListApiView.as_view(), name='device_list'),
    path('<str:device_id>/', DeviceDetailApiView.as_view(), name='device_detail'),
]
