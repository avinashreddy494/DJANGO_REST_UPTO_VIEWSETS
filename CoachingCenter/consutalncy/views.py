from django.shortcuts import render
from .models import consultancy
from .serializers import consultancySerailizer
from rest_framework import mixins
from rest_framework import generics

# Create your views here.
class consultancyListView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    queryset=consultancy.objects.all()
    serializer_class=consultancySerailizer

    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
    
class consultancyDetailView(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset=consultancy.objects.all()
    serializer_class=consultancySerailizer

    def get(self,request, pk):
        return self.retrieve(request,pk)
    
    def put(self, request, pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self. destroy(request,pk)