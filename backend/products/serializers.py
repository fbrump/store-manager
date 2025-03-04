from rest_framework import serializers
from .models import Product
from accounts.serializers import UserSerializer


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    price = serializers.DecimalField(max_digits=16, decimal_places=2)
    is_active = serializers.BooleanField(default=True,)
    # created_by = serializers.StringRelatedField(many=False)
    # created_by = serializers.PrimaryKeyRelatedField(many=False,read_only=True,)
    # created_by = serializers.SlugRelatedField(many=False,read_only=True, slug_field='username',)
    # created_by = UserSerializer(many=False, read_only=True)
    created_by = serializers.SlugRelatedField(many=False,read_only=True, slug_field='username',)
    class Meta:
        model = Product
        fields = [
            'url', 'code', 'name', 'description', 'price', 'price_currency', 'is_active', 
            'created_at', 'updated_at', 'created_by',]
        read_only_fields = ['url', 'created_at', 'updated_at',]
