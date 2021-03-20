from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE, SET_NULL

class Bill(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = CASCADE,
        related_name= "user",
        related_query_name= "users"
    )
    provider = models.ForeignKey(
        "Provider",
        on_delete = CASCADE,
        related_name= "Providers",
        related_query_name= "Provider"
    )
    bill_date = models.DateField()
    acct_number = models.CharField(max_length=30)
    name_on_acct = models.CharField(max_length=55)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    least_amount = models.DecimalField(max_digits=20, decimal_places=2)
