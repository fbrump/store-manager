from rest_framework import routers

from . import views


app_name='accounts'

router = routers.SimpleRouter()

router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)

urlpatterns = router.urls
