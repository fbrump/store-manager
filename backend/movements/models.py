import uuid

from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Transaction(models.Model):
    class TransactionTypeOptions(models.TextChoices):
        IN = 'IN'
        OUT = 'OUT'
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.IntegerField()
    type = models.CharField(
        max_length=3,
        choices=TransactionTypeOptions,
        default=TransactionTypeOptions.IN,
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.product} - {self.type} - {self.amount}'
