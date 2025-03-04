from rest_framework import serializers
from .models import Product, ProductCategory


class ProductCategorySerializer(serializers.HyperlinkedModelSerializer):
    is_active = serializers.BooleanField(default=True,)
    created_by = serializers.SlugRelatedField(many=False,read_only=True, slug_field='username',)
    class Meta:
        model = ProductCategory
        fields = [
            'id', 'url', 'name', 'description', 'is_active',
            'created_at', 'updated_at', 'created_by',]
        read_only_fields = ['id', 'url', 'created_at', 'updated_at',]

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    price = serializers.DecimalField(max_digits=16, decimal_places=2)
    is_active = serializers.BooleanField(default=True,)
    created_by = serializers.SlugRelatedField(many=False,read_only=True, slug_field='username',)
    class Meta:
        model = Product
        fields = [
            'id', 'url', 'code', 'name', 'description', 'price', 'price_currency', 'is_active', 
            'category', 'created_at', 'updated_at', 'created_by',]
        read_only_fields = ['id', 'url', 'created_at', 'updated_at',]
