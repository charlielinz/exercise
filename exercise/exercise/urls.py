from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('practice/', include('practice.urls')),
    path('', RedirectView.as_view(url='/practice/'), name='index'),
]
