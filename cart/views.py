from django.shortcuts import render
from cart.models import Cart
from products.models import Product
from django.shortcuts import get_object_or_404

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)

    return render(request, "carts/home.html", {})
