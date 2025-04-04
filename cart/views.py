from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from store.models import Product
from .cart import Cart

# Create your views here.

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    
    if quantity > 0:
        cart.add(product=product, quantity=quantity, update_quantity=False)
        # You might want to add a success message here using django.contrib.messages
    return redirect(request.META.get('HTTP_REFERER', 'home')) # Redirect back to previous page or home

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    # Add total price calculation
    for item in cart:
        item['total_price'] = item['price'] * item['quantity']
    cart_total_price = sum(item['price'] * item['quantity'] for item in cart)
    
    return render(request, 'cart/detail.html', {'cart': cart, 'cart_total_price': cart_total_price})
