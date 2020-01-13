from django.urls import path
from .views import index, add_item, delete_item

urlpatterns = [
    path('', index),
    path('add-item', add_item),
    path('delete-item/<int:item_id>', delete_item),
]