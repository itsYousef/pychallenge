from django.db import models
from django.utils import timezone
import datetime


class Device(models.Model):
    id = models.CharField(max_length=100)
    device_model = models.CharField(max_length=100)