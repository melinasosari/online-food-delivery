from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderCreateForm 
from .models import Order, OrderItem 
from cart.cart import Cart 
from django.urls import reverse 
from django.conf import settings 
from django.http import HttpResponse 
from django.contrib.admin.views.decorators import staff_member_required
from django.template.loader import render_to_string 
from django.contrib.auth.decorators import login_required

@login_required 
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, food=item['food'], price=item['price'], quantity=
                item['quantity'])
            cart.clear()
            return render(request, 'order/order_success.html', {'order':order})
    else:
        form = OrderCreateForm()
    return render(request, 'order/order_create.html', {"form":form, 'cart':cart})


@staff_member_required 
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/order/order_detail.html', {'order':order})