from django.shortcuts import render, HttpResponse
from goods.models import Goods, Cart
from .models import Order, OrderDetail
# Create your views here.
from user.models import UserProfile,UserAddress
import json
import random


def details(request,detail_id):
    detail = Goods.objects.get(id=detail_id)
    # print(detail)
    dictObj = {
        'name': detail.name,
        'image': detail.image,
        'barcode': detail.barcode,
        'price': detail.price,
        'details': detail.details,
        'market_price': detail.market_price,
        'cost_price': detail.cost_price,
        'count': detail.count,
    }

    return render(request, 'order/details.html', dictObj)


def shopping_cart(request):

    user_id = request.session.get('user_id')
    print('user_id', user_id)
    user = UserProfile.objects.filter(id=user_id).first()
    print(user)
    cartDict = {
        'price': request.GET.get('price'),
        'cost_price': request.GET.get('cost_price'),
        'details': request.GET.get('details'),
        'num': request.GET.get('num'),
        'image': request.GET.get('image'),
        'user': user
    }
    cartList = Cart.objects.filter(price=cartDict['price'], cost_price=cartDict['cost_price'],
                                   details=cartDict['details'], image=cartDict['image'], user=cartDict['user']).first()
    if cartList:
        print('已有该产品')

    else:
        cart = Cart.objects.create(price=cartDict['price'], cost_price=cartDict['cost_price'],
                                   details=cartDict['details'], num=cartDict['num'], image=cartDict['image'], user=cartDict['user'])
    car_num = Cart.objects.filter(user=user).all()
    print(car_num)
    num_count = 0
    for item in car_num:
        num_count += item.num
    print(num_count)
    a = HttpResponse(num_count)

    a['Access-Control-Allow-Origin'] = "http://localhost:8000"

    # 允许你携带Content-Type请求头
    a['Access-Control-Allow-Headers'] = "*"
    return a


def num_count(request):
    user_id = request.session.get('user_id')
    print('user_id', user_id)
    user = UserProfile.objects.filter(pk=user_id).first()
    car_num = Cart.objects.filter(user=user).all()
    print(car_num)
    num_count = 0
    for item in car_num:
        num_count += item.num
    print(num_count)
    a = HttpResponse(num_count)

    a['Access-Control-Allow-Origin'] = "http://localhost:8000"

    # 允许你携带Content-Type请求头
    a['Access-Control-Allow-Headers'] = "*"
    return a


def confirm(request):
    user_id = request.session.get('user_id')
    user = UserProfile.objects.filter(pk=user_id).first()
    order = Order.objects.filter(user=user).first()
    orderdetail = OrderDetail.objects.filter(order=order).all()
    return render(request,'order/confirm.html',{'order':order,'orderdetail':orderdetail})

def message(request):
    data = request.GET
    user_id = request.session.get('user_id')
    user = UserProfile.objects.filter(pk=user_id).first()
    address = UserAddress.objects.filter(user=user).first()
    cart = Cart.objects.filter(user=user,details=data['details']).first()
    order = Order.objects.create(
        user=user,order_no=random.randint(100000,999999),total_price=data['zongjia'],mobile=user.mobile,address=address.address,create_time=data['time'],status=0,remark='尽快发货',name=user.username)
    orderdetail = OrderDetail.objects.create(order=order,cart=cart,price=data['zongjia'],count=data['num'])
    a = HttpResponse('ok')
    a['Access-Control-Allow-Origin'] = "http://localhost:8000"

    # 允许你携带Content-Type请求头
    a['Access-Control-Allow-Headers'] = "*"
    return a 
