from django.contrib import admin
from django.urls import path
from .views import consultancyListView,consultancyDetailView
urlpatterns = [
    path('consultancy/', consultancyListView.as_view(),name="jobs"),
    path('consultancy/<int:pk>',consultancyDetailView.as_view(),name="jobdetail")
    #path('courses/<int:pk>',courseDetailView,name="courseDetailView")
]