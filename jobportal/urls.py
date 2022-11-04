"""jobportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from turtle import settiltangle
from xml.dom.minidom import Document
from django.conf import settings
from django.contrib import admin
from django.urls import path
from job.views import *
from django.conf import settings
from django.conf.urls.static import serve
from django.conf.urlsimport url


urlpatterns = [
    path('admin/', admin.site.urls),
path('', index,name="index"),
path('admin_login', admin_login ,name="admin_login"),
path('user_signup', user_signup ,name="user_signup"),
path('candidatepage', candidatepage ,name="candidatepage"),
path('employerpage', employerpage ,name="employerpage"),
path('employerdetail', employerdetail ,name="employerdetail"),
path('employerdel', employerdel ,name="employerdel"),
path('employerjobs', employerjobs ,name="employerjobs"),
path('employerlogout', employerlogout ,name="employerlogout"),
path('employerpage', employerpage ,name="employerpage"),
path('employerprofile', employerprofile ,name="employerprofile"),
path('employerpw', employerpw ,name="employerpw"),
path('employershortlist', employershortlist ,name="employershortlist"),
path('employersubmit', employersubmit ,name="employersubmit"),

path('candappjobs', candappjobs ,name="candappjobs"),
path('canddel', canddel ,name="canddel"),
path('candlogout', candlogout ,name="candlogout"),
path('candprofile', candprofile ,name="candprofile"),
path('candpw', candpw ,name="candpw"),
path('candidatepage', candidatepage ,name="candidatepage"),
path('candresume', candresume ,name="candresume"),
path('candshortjobs', candshortjobs ,name="candshortjobs"),
path('canduser', canduser ,name="canduser"),
path('hirefreelancer', hirefreelancer ,name="hirefreelancer"),
 url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
