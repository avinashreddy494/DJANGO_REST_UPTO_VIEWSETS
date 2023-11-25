from rest_framework import serializers
from .models import Instructor,stacks

'''
class stackSerializer(serializers.ModelSerializer):
    class Meta:
        model=stacks
        fields="__all__"

class instructorSerailizer(serializers.ModelSerializer):
    stacks=stackSerializer(many=True,read_only=True)
    class Meta:
        model=Instructor
        fields="__all__"
'''
class stackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=stacks
        fields="__all__"

class instructorSerailizer(serializers.HyperlinkedModelSerializer):
    stacks=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name="stack-detial")
    class Meta:
        model=Instructor
        fields=['name','stacks']