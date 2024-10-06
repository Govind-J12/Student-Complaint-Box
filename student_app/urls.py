"""
URL configuration for complaintbox project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('viewprofile',views.viewprofile),
    path('logout',views.logout),
    path('comregister',views.comregister),
    path('mycomplaints',views.mycomplaints),
    path('cdelete/<int:id>',views.cdelete,name="cdelete"),
    path('viewuserack',views.viewuserack),
    path('home',views.home),
    path('adelete/<int:id>',views.adelete,name="adelete"),
    path('comupdate/<int:id>',views.comupdate,name="comupdate"),
    path('comupdate/comupdates/<int:id>',views.comupdates,name="comupdates"),



    



    




    
    
    
]
