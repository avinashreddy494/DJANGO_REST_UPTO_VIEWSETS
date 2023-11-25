from django.shortcuts import render
from .models import stacks,Instructor
from .serializers import stackSerializer,instructorSerailizer
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
# Create your views here.

class InstructorViewset(ModelViewSet):
    queryset=Instructor.objects.all()
    serializer_class=instructorSerailizer

class stackViewset(ModelViewSet):
    queryset=stacks.objects.all()
    serializer_class=stackSerializer

class stackdDetialView(generics.RetrieveUpdateDestroyAPIView):
    queryset=stacks.objects.all()
    serializer_class=stackSerializer

class InstructorDetialView(generics.RetrieveUpdateDestroyAPIView):
    queryset=stacks.objects.all()
    serializer_class=stackSerializer