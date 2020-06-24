from django.urls import path
from .views import index, persons_detail, add_detail


app_name = 'practice'
urlpatterns = [
    path('', index, name='index'),
    path('persons_detail/<int:id>/', persons_detail, name='persons_detail'),
    path('add_detail/', add_detail, name='add_detail')
]
