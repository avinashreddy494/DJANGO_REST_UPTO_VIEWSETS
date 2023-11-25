from django.shortcuts import render
from rest_framework.viewsets import ViewSet,ModelViewSet
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from .serializers import admissionSerailizer
from .models import admission


class admissionViewset(ModelViewSet):
    queryset=admission.objects.all()
    serializer_class=admissionSerailizer








'''
class admissionViewset(ViewSet):
    print("eneted")
    def list(self,request):
        admissions=admission.objects.all()
        serializer=admissionSerailizer(admissions,many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer=admissionSerailizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self,request,pk):
        try:
            admissions=admission.objects.get(pk=pk)
        except admission.DoesNotExist:
            raise Http404
        serailizer=admissionSerailizer(admissions)
        return Response(serailizer.data)
'''
    