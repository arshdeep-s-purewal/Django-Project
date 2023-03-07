"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.views.decorators.csrf import csrf_exempt
from blog.views import create_blog, index, list_blogs, delete_blog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',csrf_exempt(index),name='index'),
    path('blogs/create',csrf_exempt(create_blog),name='create_blog'),
    path('blogs/list', list_blogs),
    path('blogs/<int:pk>/delete/', delete_blog),
    
]
