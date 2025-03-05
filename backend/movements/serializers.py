from rest_framework import serializers
from .models import Transaction
from products.models import Product


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    is_active = serializers.BooleanField(default=True,)
    product = serializers.SlugRelatedField(many=False,read_only=False, slug_field='code', queryset=Product.objects.all())
    created_by = serializers.SlugRelatedField(many=False,read_only=True, slug_field='username',)
    class Meta:
        model = Transaction
        fields = [
            'id', 'url', 'product', 'type', 'amount', 'is_active', 
            'created_at', 'updated_at', 'created_by',]
        read_only_fields = ['id', 'url', 'created_at', 'updated_at',]
