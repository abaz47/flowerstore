from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('flowers.urls', namespace='flowers')),
    path('admin/', admin.site.urls),
]
