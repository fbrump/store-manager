from rest_framework import routers

from . import views


app_name='movements'

router = routers.SimpleRouter()

router.register('transactions', views.TransactionViewSet)
router.register('transactions-count', views.TransactionTopViewSet, basename='counts')

urlpatterns = router.urls
