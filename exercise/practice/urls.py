from django.urls import path
from .views import index, persons_detail, add_detail, edit_detail, delete_detail


app_name = 'practice'
urlpatterns = [
    path('', index, name='index'),
    path('persons_detail/<int:id>/', persons_detail, name='persons_detail'),
    path('add_detail/', add_detail, name='add_detail'),
    path('edit_detail/', edit_detail, name='edit_detail'),
    path('delete_detail/<int:id>/', delete_detail, name='delete_detail'),
]
