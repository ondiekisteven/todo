from django.urls import path
from .views import index, add_item, delete_item, list_items, get_item
from users.views import profile

urlpatterns = [
    path('', index, name='auth-list'),
    path('add-item/', add_item, name='add-item'),
    path('delete-item/<int:item_id>', delete_item),
    path('api/', list_items),
    path('api/<int:item_id>', get_item),
]
