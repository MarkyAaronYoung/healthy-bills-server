from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL

class Provider(models.Model):
    provider_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=25)
