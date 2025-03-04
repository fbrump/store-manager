from rest_framework import routers

from . import views


app_name='products'

router = routers.SimpleRouter()

router.register('products', views.ProductViewSet)

urlpatterns = router.urls
