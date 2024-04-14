from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView 
from .models import Category, Food 
from cart.forms import CartAddFoodForm


class HomeView(TemplateView):
    template_name = 'menu/home.html'
    
    
def food_list(request, category_slug=None):
    category = None 
    categories = Category.objects.all()
    foods = Food.objects.all()
    cart_food_form = CartAddFoodForm()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        foods = foods.filter(category=category)
    context = {
        'categories':categories,
        'category':category,
        'foods':foods,
        'form':cart_food_form
    }
    return render(request, 'menu/food_list.html', context)

def food_detail(request, id, slug):
    food = get_object_or_404(Food, id=id, slug=slug)
    cart_food_form = CartAddFoodForm()
    context = {
        'food':food,
        'form':cart_food_form
    }
    return render(request, 'menu/food_detail.html', context)
