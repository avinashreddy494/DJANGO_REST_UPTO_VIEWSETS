from django.shortcuts import render
from .models import Jobs
from .serializers import JobSerializer
from  rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from django.http import Http404
from rest_framework import status


class JobListView(APIView):
    def get(self,request):
        jobs=Jobs.objects.all()
        serializer=JobSerializer(jobs,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serailizer=JobSerializer(data=request.data)
        if serailizer.is_valid():
            serailizer.save()
            return Response(serailizer.data)
        return Response(serailizer.errors)

class JobDetailView(APIView):

    def get_job(self,pk):
        try:
            return Jobs.objects.get(pk=pk)
        except Jobs.DoesNotExist:
            raise Http404
        
    def get(self,request,pk):
        job=self.get_job(pk)
        serializer=JobSerializer(job)
        return Response(serializer.data)
    
    def put(self,request,pk):
        job=self.get_job(pk)
        serailizer=JobSerializer(job,data=request.data)
        if serailizer.is_valid():
            serailizer.save()
            return Response(serailizer.data)
        return Response(serailizer.errors)
        
    def delete(self,request,pk):
        job=self.get_job(pk)
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)