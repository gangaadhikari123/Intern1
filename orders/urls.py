from django.urls import path
from . import views

urlpatterns = [
    path('history/', views.order_history, name='order_history'),
    path("cart/", views.cart, name="cart"),
    path("add/<int:id>/", views.add_to_cart, name="add_to_cart"),
]
