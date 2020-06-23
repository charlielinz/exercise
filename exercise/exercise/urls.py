from django.contrib import admin
from django.urls import path
from .views import index, info


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('info/', info, name='info')
]
