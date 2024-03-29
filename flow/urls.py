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
from posts.views import post_list, post_detail, post_new, add_comment, delete_post, edit_comment, edit_post
from allauth.urls import *
from allauth import urls as allauth_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(allauth_urls), name='account'),
    path('post/new/', post_new, name='post_new'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('post/<int:post_id>/add_comment/', add_comment, name='add_comment'),
    path('post/<int:post_id>/add_comment/<int:parent_comment_id>/', add_comment, name='add_comment_reply'), 
    path('post/<int:post_id>/edit_comment/<int:comment_id>/', edit_comment, name='edit_comment'),
    path('post/<int:post_id>/delete/', delete_post, name='delete_post'),
    path('edit_post/<int:post_id>/', edit_post, name='edit_post'),
    path('', post_list, name='post_list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
