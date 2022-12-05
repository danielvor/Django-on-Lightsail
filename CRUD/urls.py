from django.urls import path
from CRUD import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),
    # Add Product
    path('add_product', views.add_product, name='add_product'),
    # View the Product Indivually
    path('product/<str:product_id>', views.product, name='product'),
    # Edit Product
    path('edit_product/', views.edit_product, name='edit_product'),
    # Delete Product
    path('delete_product/<str:product_id>', views.delete_product, name='delete_product'),
]
