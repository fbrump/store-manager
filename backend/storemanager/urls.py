from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views


urlpatterns = [
    path('v1/accounts/', include('accounts.urls')),
    path('v1/', include('products.urls')),
    path('v1/', include('movements.urls')),
    path('v1/api-auth/', include('rest_framework.urls')),
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('admin/', admin.site.urls),
]
