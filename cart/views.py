from django.shortcuts import render
from cart.models import Cart
def cart_home(request):
    # del request.session['cart_id']
    cart_id = request.session.get('cart_id', None)
    if cart_id is None: #and isinstance(cart_id, int):
        cart_obj = Cart.objects.create()
        request.session['cart_id'] = cart_obj.id
        print('New cart created')
    else:
        print('Cart ID is exist')
        print(cart_id)
        cart_obj = Cart.objects.get(id=cart_id)

    # print(request.session)
    # print(dir(request.session))
    # request.session['f_name'] = "Amir Savvy" # Session Setter
    return render(request, "carts/home.html", {})
