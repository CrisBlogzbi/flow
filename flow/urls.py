"""
URL configuration for flow project.

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
from django.urls import path, include
from posts.views import post_list, post_detail, post_new, add_comment
from allauth.urls import *
from allauth import urls as allauth_urls


import allauth.urls

from allauth.urls import urlpatterns as allauth_urls
path('accounts/', include(allauth_urls))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(allauth.urls)),
    path('post/new/', post_new, name='post_new'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('post/<int:post_id>/add_comment/', add_comment, name='add_comment'), 
    path('', post_list, name='post_list'),
]
