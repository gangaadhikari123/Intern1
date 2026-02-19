from django.shortcuts import render, redirect
from .models import Order, OrderItem
from products.models import Product

def cart(request):
    return render(request, "orders/cart.html")


def add_to_cart(request, id):
    product = Product.objects.get(id=id)
    order, created = Order.objects.get_or_create(id=1)
    OrderItem.objects.create(order=order, product=product)
    return redirect("cart")
