# -*- coding: UTF-8 -*-
"""DAI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from DAI import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login/', views.login, name='login'),
    url(r'^logout/',views.logout, name='logout'),
    url(r'^inscripcion/', views.inscripcion, name='inscripcion'),
    #url(r'^perfil/',views.perfil, name='perfil'),
    url(r'^editar/',views.editar,name='editar'),
    url(r'^armaduras/',views.armaduras, name='armaduras'),
    url(r'^armaduragen/',views.armaduragen,name='armaduragen'),
    url(r'^mostrararmaduras$',views.mostrararmaduras,name='mostrararmaduras'),
    url(r'^reclama_datos/$',views.reclama_datos,name='reclama_datos'),
    url(r'^grafica',views.grafica,name='grafica'),
    url(r'^admin/', admin.site.urls),
]
