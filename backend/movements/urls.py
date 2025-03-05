from rest_framework import routers

from . import views


app_name='movements'

router = routers.SimpleRouter()

router.register('transactions', views.TransactionViewSet)

urlpatterns = router.urls
