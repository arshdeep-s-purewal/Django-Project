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
from blog.views import create_blog, list_blogs, delete_blog, update_blog, create_new_user, index_page, login_user,logout_user, BlogView, BlogList
from apna_bazaar.views import add_product,show_products, show_product_detail, add_to_cart,remove_from_cart,home_ecom,register_user,login_ecom
urlpatterns = [
    # path('', index_page,name='index'),
    path('', home_ecom,name='index'),
    path('admin/', admin.site.urls),
    path('blogs/create',BlogView.as_view(),name='create_blog'),
    # path('blogs/create',csrf_exempt(create_blog),name='create_blog'),
    # path('blogs/list', list_blogs, name='list_blogs'),
    path('blogs/list', BlogList.as_view(), name='list_blogs'),
    path('blogs/<int:pk>/delete/', delete_blog, name='delete_blogs'),
    path('blogs/<int:pk>/edit/', update_blog,name='edit_blog'),
    path('apna_bazaar/add_product/', add_product),
    path('apna_bazaar/show_products', show_products, name='show_products'),
    path('apna_bazaar/<int:pk>/detail_of_products', show_product_detail),
    path('apna_bazaar/<int:pk>/add_to_cart', add_to_cart),
    path('apna_bazaar/<int:pk>/remove_from_cart', remove_from_cart),
    path('blogs/create_new_user', create_new_user,name='create_new_user'),
    path('blogs/login', login_user, name="login"),
    path('blogs/logout', logout_user, name="logout"),
    path('apna_bazaar/register_user', register_user, name='register_ecom'),
    path('apna_bazaar/login_user', login_ecom, name='login_ecom'),
]
