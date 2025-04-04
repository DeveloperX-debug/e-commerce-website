from django.shortcuts import render
from .models import Product

# Create your views here.

def home(request):
    """View function for the home page, displaying all products."""
    products = Product.objects.all() # Get all product objects from the database
    context = {
        'products': products,
    }
    # Render the HTML template store/home.html with the data in context
    return render(request, 'store/home.html', context)

# Add views for product details, cart, checkout later
