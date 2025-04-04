from django.contrib import admin
from .models import Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'team', 'price', 'stock', 'created_at')
    list_filter = ('team', 'stock')
    search_fields = ('name', 'description', 'team')
    list_editable = ('price', 'stock')  # Allow quick editing of stock levels from list view
