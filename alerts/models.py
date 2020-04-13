from django.db import models

# Create your models here.

class AlertItem(models.Model):
    message = models.TextField()
    state = models.CharField(max_length=50)
    dashboardId = models.IntegerField()

    def __str__(self):
        return str(self.dashboardId) + "-" + self.message
    