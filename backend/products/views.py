import logging
from rest_framework import permissions, viewsets, versioning
from rest_framework.response import Response
from .models import Product, ProductCategory
from .serializers import ProductSerializer, ProductCategorySerializer


_logger = logging.getLogger(__name__)

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to view or edit product.
    """
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    versioning_class = versioning.NamespaceVersioning
    def create(self, request):
        serializer = ProductSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=request.user)
        return Response(serializer.data)

class ProductCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to view or edit product category.
    """
    queryset = ProductCategory.objects.all().order_by('-created_at')
    serializer_class = ProductCategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    versioning_class = versioning.NamespaceVersioning
    def create(self, request) -> Response:
        _logger.debug('[ Product Category ] Start to create a new category')
        serializer = ProductCategorySerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=request.user)
        _logger.debug('[ Product Category ] Complete to create a new category')
        _logger.warning('[ Product Category ] Serializer: %s', serializer)
        return Response(serializer.data)
