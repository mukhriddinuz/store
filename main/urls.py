from django.urls import path
from .views import *


urlpatterns = [
    path('', index_view, name='index_url'),
    path('product-detail/<int:pk>/', product_detail, name='product_detail_url'),
    path('products/', product, name='product_url'),
    path('create_total_sum/', create_total_sum, name='create_total_sum_url'),
    path('cart/<int:pk>/', cart, name='cart_url'),
    path('add_basket/<int:pk>/', add_basket, name='add_basket_url'),
    path('add_basket_form/<int:pk>/', add_basket_form, name='add_basket_form_url'),
    path('remove_cart_product/<int:pk>/', remove_cart_product, name='remove_cart_product_url'),
#     path('login/', login_view, name='login_url'),
#     path('sing-up/', sing_up_view, name='sing_up_url'),
#     path('logout/', user_logout, name='logout_url'),
]