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
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('viewstudents',views.viewstudents),
    path('faculty',views.faculty),
    path('ddelete/<int:id>',views.ddelete,name="ddelete"),
    path('viewfaculty',views.viewfaculty),
    path('adminackno',views.adminackno),
    path('fdelete/<int:id>',views.fdelete,name="fdelete"),
    path('admincomview',views.admincomview),
    path('acdelete/<int:id>',views.acdelete,name="acdelete"),
    path('adminindex',views.adminindex),
    path('stdupdate/<int:id>',views.stdupdate,name="stdupdate"),
    path('stdupdate/stdupdates/<int:id>',views.stdupdates,name="stdupdates"),
    path('facupdate/<int:id>',views.facupdate,name="facupdate"),
    path('facupdate/facupdates/<int:id>',views.facupdates,name="facupdates"),


    

    
]
