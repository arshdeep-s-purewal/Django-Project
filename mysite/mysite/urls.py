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
from django.conf import settings
from django.conf.urls.static import static
from blog.views import create_blog, list_blogs, delete_blog, update_blog, create_new_user, index_page, login_user,logout_user, BlogView, BlogList
from apna_bazaar.views import add_product,show_products_listing, show_product_detail, add_to_cart,remove_from_cart,home_ecom,register_user,login_ecom, logout_user_ecom,success,home,show_cart, add_to_wishlist, show_wishlist, remove_from_wishlist, checkout, shipping_details, userprofile, ordered
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
    path('blogs/create_new_user', create_new_user,name='create_new_user'),
    path('blogs/login', login_user, name="login"),
    path('blogs/logout', logout_user, name="logout"),
    path('apna_bazaar/add_product/', add_product, name='add_product_image'),
    path('apna_bazaar/show_products', show_products_listing, name='show_products'),
    path('apna_bazaar/<int:pk>/detail_of_products', show_product_detail, name= 'detail_of_products'),
    path('apna_bazaar/<int:pk>/add_to_cart', add_to_cart),
    path('apna_bazaar/<int:pk>/remove_from_cart', remove_from_cart),
    path('apna_bazaar/register_user', register_user, name='register_ecom'),
    path('apna_bazaar/login_user', login_ecom, name='login_ecom'),
    path('apna_bazaar/logout_user', logout_user_ecom, name='logout_ecom'),
    path('success', success, name='success'),
    path('apna_bazaar/homepage', home, name='homepage'),
    path('apna_bazaar/cart', show_cart, name='cart'),
    path('apna_bazaar/<int:pk>/add_to_wishlist', add_to_wishlist, name='add_to_wishlist'),
    path('apna_bazaar/wishlist', show_wishlist, name='wishlist'),
    path('apna_bazaar/<int:pk>/remove_wishlist', remove_from_wishlist),
    path('apna_bazaar/checkout', checkout, name='checkout'),
    path('apna_bazaar/shipping_details', shipping_details, name='shipping_address'),
    path('apna_bazaar/profile_page', userprofile, name='profile_page'),
    path('apna_bazaar/order_placed', ordered, name='ordered'),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
