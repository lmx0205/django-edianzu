from django.shortcuts import render, HttpResponse
from goods.models import Goods, Cart
from django.db.models import Q


def index(request):
    proList1 = Goods.objects.filter(hello='热销机型')
    proList2 = Goods.objects.filter(hello='行政办公')
    proList3 = Goods.objects.filter(hello='技术开发')
    proList4 = Goods.objects.filter(hello='商务便携')
    proList5 = Goods.objects.filter(hello='图形处理')
    proList6 = Goods.objects.filter(hello='外设配件')
    dictObj = {
        'proList1': proList1,
        'proList2': proList2,
        'proList3': proList3,
        'proList4': proList4,
        'proList5': proList5,
        'proList6': proList6,
    }
    return render(request, 'index/index.html', dictObj)


def search(request):
    categorys = Goods.objects.values('name').distinct()
    tags = Goods.objects.values('unit').distinct()
    key = request.GET.get('key')
    error_msg = ''

    if not key:
        error_msg = '请输入关键词'
        return render(request, 'goods/categoryList.html', {'goods': error_msg, 'categorys': categorys, 'tags': tags, 'good_name': '笔记本'})

    post_list = Goods.objects.filter(Q(name__icontains=key) | Q(keywords__icontains=key) | Q(
        unit__icontains=key) | Q(barcode__icontains=key) | Q(details__icontains=key))
    print('方法', post_list)

    return render(request, 'goods/categoryList.html', {'goods': post_list, 'categorys': categorys, 'tags': tags, 'good_name': '笔记本'})
