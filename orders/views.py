from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, OrderItem
from products.models import Product
from django.contrib.auth.decorators import login_required


# View cart
@login_required
def cart(request):
    order, created = Order.objects.get_or_create(user=request.user, status="pending")
    items = OrderItem.objects.filter(order=order)

    return render(request, "orders/cart.html", {
        "order": order,
        "items": items
    })


# Add product to cart
@login_required
def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)

    order, created = Order.objects.get_or_create(
        user=request.user,
        status="pending"
    )

    OrderItem.objects.create(
        order=order,
        product=product,
        quantity=1
    )

    return redirect("cart")


# Checkout
@login_required
def checkout(request):
    order = Order.objects.get(user=request.user, status="pending")

    items = OrderItem.objects.filter(order=order)

    for item in items:
        product = item.product

        if product.stock < item.quantity:
            return render(request, "orders/cart.html", {
                "error": f"{product.name} is out of stock"
            })

        product.stock -= item.quantity
        product.save()

    order.status = "completed"
    order.save()

    return redirect("order_history")


# Order history
@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user, status="completed")

    return render(request, "orders/order_history.html", {
        "orders": orders
    })
