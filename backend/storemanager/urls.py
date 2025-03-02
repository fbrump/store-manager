from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('v1/accounts/', include('accounts.urls', namespace='v1')),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
