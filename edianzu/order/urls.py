from django.urls import path, include
from . import views

urlpatterns = [
    path('details/<int:detail_id>', views.details,name='details'),
    path('details/shopping_cart', views.shopping_cart,name='shopping_cart'),
    path('details/num_count', views.num_count),
    path('details/confirm', views.confirm,name='confirm'),
    path('message/', views.message,name='message'),
]
