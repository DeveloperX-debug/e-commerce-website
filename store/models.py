from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2, default=199.00)
    # Use ImageField for actual image uploads later, CharField for URLs now
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    team = models.CharField(max_length=100)
    # Add stock count if needed later
    stock = models.IntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
