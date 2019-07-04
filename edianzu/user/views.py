from django.shortcuts import render, redirect, HttpResponse
from .models import UserProfile, UserAddress
from order.models import Order, OrderDetail
from goods.models import Cart,Goods

# 注册页面


def register(request):
    if request.method == "POST":
        tel = request.POST.get('tel')
        message = request.POST.get('message')
        pw = request.POST.get('pw')
        print(tel, message, pw)
        if tel and message and pw:
            print('注册成功！！')
            user = UserProfile.objects.create(
                mobile=tel, password=pw, username=tel)
            user.save()
            return redirect('/user/login/')
        else:
            print('信息有误，请重新输入！')
    return render(request, 'login_register/register.html')

# 登录页面


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pw = request.POST.get('pw')
        tel = request.POST.get('tel')
        message = request.POST.get('message')
        try:
            user = UserProfile.objects.get(
                username=username, password=pw) or UserProfile.objects.get(mobile='tel')
            print('user', user)
            if user:
                print('登录成功！')
                request.session['user_id'] = user.pk
                # request.session.set_expiry()
                return redirect('/user/user_center/')
            else:
                print('登录失败！')
        except:
            print('登录失败！')

    return render(request, 'login_register/login.html')

# 个人中心


def user_center(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = UserProfile.objects.filter(pk=user_id).first()
        print('user', user)
        return render(request, 'user/user_center.html', {'user': user})
    else:
        return redirect('/user/login/')

# 个人资料


def user_info(request):
    user_id = request.session.get('user_id')
    user = UserProfile.objects.filter(pk=user_id).first()
    return render(request, 'user/user_info.html', {'user': user})

# 我的订单


def user_order(request):
    user_id = request.session.get('user_id')
    user = UserProfile.objects.filter(pk=user_id).first()
    carts = Cart.objects.filter(user=user).all()

    return render(request, 'user/user_order.html', {'carts': carts})

# 快递地址


def user_address(request):
    user_id = request.session.get('user_id')
    user = UserProfile.objects.get(pk=user_id)
    print(user)
    Address = UserAddress.objects.filter(user=user)
    print(Address)
    return render(request, 'user/user_address.html', {'Address': Address})

# 新增快递地址


def user_address_add(request):
    user_id = request.session.get('user_id')
    user = UserProfile.objects.filter(pk=user_id).first()
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        if name and mobile and address:
            Address = UserAddress.objects.create(
                name=name, mobile=mobile, address=address, user=user)
            return redirect('/user/user_center/user_address/')
        else:
            print('输入不能为空')
    return render(request, 'user/user_address_add.html')

# 退出登录


def logout(request):
    request.session.clear()
    return redirect('/user/login/')



# 购物车
def cart(request):
    user_id = request.session.get('user_id')
    user = UserProfile.objects.filter(pk=user_id).first()
    print(user)
    result = Cart.objects.filter(user=user).all()
    print(result)
    return render(request, 'user/cart.html', {'result': result})

# 删除购物车
def del_car(request,del_id):
    user_id = request.session.get('user_id')
    user = UserProfile.objects.filter(pk=user_id).first()
    del_result = Cart.objects.filter(user=user,pk=del_id).delete()
    result = Cart.objects.filter(user=user).all()
    return render(request, 'user/cart.html', {'result': result})


# def cartList(request):
#     resList = []
#     for item in result:
#         item['_id'] = str(item['_id'])
#         resList.append(item)

#     jsonStr = json.dumps(resList, ensure_ascii=False)

#     a = HttpResponse(jsonStr)

#     a['Access-Control-Allow-Origin'] = "*"

#     a['Access-Control-Allow-Headers'] = "*"
#     return a
