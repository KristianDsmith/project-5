from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>',
         views.order_history, name='order_history'),
    # View the user's wishlist
    path('wishlist/', views.view_wishlist, name='view_wishlist'),
    path('wishlist/add/<product_id>/', views.add_to_wishlist,
         name='add_to_wishlist'),  # Add a product to the wishlist
    path('remove_from_wishlist/<int:product_id>/',
         views.remove_from_wishlist, name='remove_from_wishlist'),
]
