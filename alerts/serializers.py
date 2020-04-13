from rest_framework import serializers
from .models import AlertItem

class AlertItemSerializer(serializers.ModelSerializer):

    class Meta:
        model=AlertItem
        fields='__all__'