from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    item_content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.item_content
