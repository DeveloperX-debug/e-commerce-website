from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# Define URL patterns for the store app
urlpatterns = [
    # Path for the home page (root of the store app)
    path('', views.home, name='home'),
    # Add paths for product details, cart, etc. later
    # path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 