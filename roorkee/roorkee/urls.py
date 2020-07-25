"""roorkee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="iit roorkee homepage"),
    path('Employee/', views.index1, name="iit roorkee homepage"),
    path('Alumni/', views.index2, name="iit roorkee page1"),
    path('Placements/', views.index3, name="iit roorkee page2"),
    path('Students/', views.index4, name="iit roorkee page3"),
    path('InternationalRelations/', views.index5, name="iit roorkee page4"),
    path('Visitors/', views.index6, name="iit roorkee page5"),
    path('Hindi/', views.index7, name="iit roorkee page6"),
    path('language/', views.index8, name="iit roorkee page7"),
    path('institute/',views.index9,name="iit roorkee page8"),
    path('academics/', views.index10, name="iit roorkee page9"),
    path('admissions/', views.index11, name="iit roorkee page10"),
    path('administrtions/', views.index12, name="iit roorkee page11"),
    path('hostals/', views.index13, name="iit roorkee page12"),
    path('departments/', views.index14, name="iit roorkee page13"),
    path('Research/', views.index15, name="iit roorkee page14"),
    path('Recruitments/', views.index16, name="iit roorkee page15"),
    path('Tenders/', views.index17, name="iit roorkee page16"),
]
