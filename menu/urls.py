from django.urls import path 
from .views import HomeView 
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('food_list/', views.food_list, name='food_list'),
    path('<slug:category_slug>', views.food_list, name='food_list_by_category'),
    path('<int:id>/<slug:slug>/', views.food_detail, name='food_detail'),
]
