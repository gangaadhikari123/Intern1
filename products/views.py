from .models import Product, Category
from django.shortcuts import render

def product_list(request):
    category_id = request.GET.get('category')

    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()

    categories = Category.objects.all()

    return render(request, "products/product_list.html", {
        "products": products,
        "categories": categories
    })
