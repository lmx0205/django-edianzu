from django.urls import path,include
from . import views

urlpatterns = [
    path('category/',views.category,name='category'),
    path('category/categoryList/<name>',views.categoryList,name='categoryList'),
    path('category/choose/',views.choose,name='choose'),
    path('category/sale/<name>',views.sale,name='sale'),
    path('category/price/<name>',views.price,name='price'),
]