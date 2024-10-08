"""
URL configuration for chats_webs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.views.generic.base import TemplateView
from chats.views import sala_chats,lobby_salas

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',index),
    path('accounts/',include('accounts.urls')),
    path('accounts/',include('django.contrib.auth.urls'),name='login'),
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
    path('lobby/rooms',lobby_salas,name='lobby'),
    path('sala/<str:sala>/',sala_chats)
]
