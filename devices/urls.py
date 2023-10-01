from django.urls import path
from .views import DeviceListApiView, DeviceDetailApiView

urlpatterns = [
    path('', DeviceListApiView.as_view()),
    path('<str:device_id>/', DeviceDetailApiView.as_view()),
]
