from django.shortcuts import render, get_object_or_404, redirect 
from django.views.decorators.http import require_POST 
from .cart import Cart 
from menu.models import Food 
from .forms import CartAddFoodForm 
from coupon.forms import CouponApplyForm

@require_POST
def cart_add(request, food_id):
    cart = Cart(request)
    food = get_object_or_404(Food, id=food_id)
    form = CartAddFoodForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add_to_cart(food=food, quantity=cd['quantity'], override_quantity=cd['override'])
    return redirect('cart_detail')


@require_POST 
def cart_remove(request, food_id):
    cart = Cart(request)
    food = get_object_or_404(Food, id=food_id)
    cart.remove_from_cart(food)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    coupon_apply_form = CouponApplyForm()
    for item in cart: 
        item['update_quantity_form'] = CartAddFoodForm(initial={
            'quantity':item['quantity'],
            'override':True
        })
    return render(request, 'cart/cart_detail.html', {'cart':cart, 'form':coupon_apply_form})
    


