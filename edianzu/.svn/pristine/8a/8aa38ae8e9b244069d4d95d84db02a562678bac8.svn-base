from django.urls import path,include
from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('user_center/',views.user_center,name='user_center'),
    path('user_center/user_info/',views.user_info,name='user_info'),
    path('user_center/user_order/',views.user_order,name='user_order'),
    path('user_center/user_address/',views.user_address,name='user_address'),
    path('user_center/user_address/user_address_add/',views.user_address_add,name='user_address_add'),
    path('user_center/logout/',views.logout,name='logout'),
    path('cart/',views.cart,name='cart'),
    path('cart/del_car/<int:del_id>',views.del_car,name='del_car'),
    # path('cartList/',views.cartList,name='cartList'),
]
