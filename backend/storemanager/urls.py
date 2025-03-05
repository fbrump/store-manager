from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('v1/accounts/', include('accounts.urls')),
    path('v1/', include('products.urls')),
    path('v1/', include('movements.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
