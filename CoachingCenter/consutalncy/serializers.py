from rest_framework import serializers
from .models import consultancy

class consultancySerailizer(serializers.ModelSerializer):
    class Meta:
        model=consultancy
        fields="__all__"