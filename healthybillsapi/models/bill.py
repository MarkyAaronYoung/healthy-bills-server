from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL

class Bill(models.model):
    user = models.ForeignKey(
        "User",
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
    amount = models.DecimalField()
    least_amount = models.DecimalField()
