from django.db import models
from django.utils import timezone
import datetime


class Device(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    device_model = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    note = models.CharField(max_length=100)
    serial = models.CharField(max_length=100)

    def __str__(self):
        return self.device_model
