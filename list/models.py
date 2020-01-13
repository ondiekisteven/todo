from django.db import models


class Item(models.Model):
    item_content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_content
