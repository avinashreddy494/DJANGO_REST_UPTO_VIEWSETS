from django.shortcuts import render
from rest_framework import generics
from .models import branch
from .serializers import branchSerializer
# Create your views here.


class branchListView(generics.ListCreateAPIView):
    queryset=branch.objects.all()
    serializer_class=branchSerializer


class branchDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=branch.objects.all()
    serializer_class=branchSerializer