from rest_framework import serializers
from .models import admission

class admissionSerailizer(serializers.ModelSerializer):
    class Meta:
        model=admission
        fields='__all__'