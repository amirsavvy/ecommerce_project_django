from django.shortcuts import render
from cart.models import Cart
from django.shortcuts import get_object_or_404

def cart_create(user=None):
    cart_obj = Cart.objects.create(user=None)
    print('New cart created')
    return cart_obj

def cart_home(request):
    # del request.session['cart_id']
    request.session['cart_id'] = '2'
    cart_id = request.session.get('cart_id', None)
    # print(cart_id)
    # if cart_id is None: #and isinstance(cart_id, int):
    #     cart_obj = cart_create()
    #     request.session['cart_id'] = cart_obj.id
    # else:
    qs = Cart.objects.filter(id=cart_id)
    if qs.count == 1:
        print('Cart ID is exist')
        cart_obj = qs.first()
    else:
        cart_obj = cart_create()
        request.session['cart_id'] = cart_obj.id    
    # cart_obj = get_object_or_404(Cart, pk=cart_id)
    # print(request.session)
    # print(dir(request.session))
    # request.session['f_name'] = "Amir Savvy" # Session Setter
    return render(request, "carts/home.html", {})
