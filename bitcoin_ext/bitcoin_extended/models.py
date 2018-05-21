from django.db import models

# Create your models here.
from django.db import models


class Address(models.Model):
    address = models.CharField(max_length=160)

    def __str__(self):
        return self.address


class Times(models.Model):
    first_date = models.PositiveIntegerField(default=None, blank=True, null=True)
    last_date = models.PositiveIntegerField(default=None, blank=True, null=True)


class Transactions(models.Model):
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    tx_index = models.CharField(max_length=64, default='tid')
    time = models.PositiveIntegerField(default=1)
    size = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.tx_index
