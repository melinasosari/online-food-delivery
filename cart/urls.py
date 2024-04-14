from django.urls import path 
from . import views 

urlpatterns = [
    path('cart_detail/', views.cart_detail, name='cart_detail'),
    path('cart_add/<int:food_id>/', views.cart_add, name='cart_add'),
    path('cart_remove/<int:food_id>/', views.cart_remove, name='cart_remove'),
]
