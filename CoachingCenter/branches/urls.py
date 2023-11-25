from django.contrib import admin
from django.urls import path
from .views import branchListView,branchDetailView
urlpatterns = [
    path('branches/', branchListView.as_view(),name="branches"),
    path('branches/<int:pk>',branchDetailView.as_view(),name="jobdetail")
    #path('courses/<int:pk>',courseDetailView,name="courseDetailView")
]