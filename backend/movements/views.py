import logging
from rest_framework import permissions, viewsets, versioning
from rest_framework.response import Response
from .models import Transaction
from .serializers import TransactionSerializer


_logger = logging.getLogger(__name__)

class TransactionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to view or edit transaction.
    """
    queryset = Transaction.objects.all().order_by('-created_at')
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
    versioning_class = versioning.NamespaceVersioning
    def create(self, request):
        serializer = TransactionSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=request.user)
        return Response(serializer.data)

class TransactionTopViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    permission_classes = [permissions.IsAuthenticated]
    versioning_class = versioning.NamespaceVersioning
    def list(self, request):
        queryset = Transaction.objects.count()
        return Response({'count': queryset })
