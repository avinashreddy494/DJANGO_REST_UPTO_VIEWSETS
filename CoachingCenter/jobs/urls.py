from django.contrib import admin
from django.urls import path
from .views import JobListView,JobDetailView
urlpatterns = [
    path('jobs/', JobListView.as_view(),name="jobs"),
    path('jobs/<int:pk>',JobDetailView.as_view(),name="jobdetail")
    #path('courses/<int:pk>',courseDetailView,name="courseDetailView")
]