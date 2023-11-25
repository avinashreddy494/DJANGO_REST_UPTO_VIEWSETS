"""
URL configuration for CoachingCenter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from admissions.views import admissionViewset
from batchone.views import stackViewset,InstructorViewset,stackdDetialView,InstructorDetialView
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('admissions',admissionViewset,basename='admissions')
router.register('instructor',InstructorViewset,basename='instructors')
router.register('stacks',stackViewset,basename='stacks')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cbse/stacks/<int:pk>',stackdDetialView.as_view(),name="stack-detial"),
    path('cbse/Instructors/<int:pk>',InstructorDetialView.as_view(),name="instructor-detail"),
    path('cbse/',include('courses.urls')),
    path('cbse/',include('jobs.urls')),#decoratoes 
    path('cbse/',include('consutalncy.urls')),#mixins
    path('cbse/',include('branches.urls')),# apiviews 
    path('cbse/',include(router.urls))
]

