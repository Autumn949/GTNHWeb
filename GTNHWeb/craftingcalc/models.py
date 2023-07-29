from django.db import models

# Create your models here.
from django.db import models


class CraftingQuery(models.Model):
    query_item = models.TextField("query_item")
    amount = models.IntegerField("amount")
    uuid = models.IntegerField("uuid")


class AuthenticatedUser(models.Model):
    # ...
    class Meta:
        permissions = (
            ("can_use_craftingcalc", "can_use_craftingcalc"),
        )