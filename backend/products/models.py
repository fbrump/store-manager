import uuid

from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    class CurrencyOptions(models.TextChoices):
        EURO = 'EUR'
        DOLLAR = 'USD'
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=30, unique=True, db_index=True)
    name = models.CharField(max_length=60, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=16, decimal_places=2)
    price_currency = models.CharField(
        max_length=3,
        choices=CurrencyOptions,
        default=CurrencyOptions.EURO,
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
