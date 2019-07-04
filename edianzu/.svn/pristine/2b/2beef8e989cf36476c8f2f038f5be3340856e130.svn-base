from django.db import models
from datetime import datetime
from user.models import UserProfile




class Goods(models.Model):
    STATUS_CHOICES = (
        (0, '下架'),
        (1, '上架'),
    )

    hello = models.CharField(max_length=500, verbose_name='产品单位')
    name = models.CharField(max_length=500, verbose_name='产品类别')
    unit = models.CharField(max_length=100, verbose_name='产品品牌')
    keywords = models.CharField(max_length=200, verbose_name='关键词')
    image = models.ImageField(upload_to='static/product/%Y/%m', verbose_name='产品图片')
    barcode = models.CharField(max_length=100, verbose_name='配置')
    price = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name='押金')
    market_price = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name='随租随还')
    cost_price = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name='租完即送')
    count = models.IntegerField(default=0, verbose_name='库存')
    sales_count = models.IntegerField(default=0, verbose_name='销量')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, verbose_name='状态')
    details = models.TextField(verbose_name='详情')

    def __str__(self):
        return '%s,%s,%s,%s,%s,%s,%s,%s'%(self.name,self.image,self.market_price,self.unit,self.hello,self.details,self.keywords,self.barcode)
    
    def __repr__(self):
        return self.__str__() 
    class Meta:
        verbose_name = '产品'
        verbose_name_plural = verbose_name
        
class Cart(models.Model):
    user = models.ForeignKey(UserProfile,null=True,blank=True,on_delete=models.CASCADE,verbose_name='用户')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='租金')
    cost_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='押金')
    details = models.TextField(verbose_name='详情')
    num = models.IntegerField(verbose_name='购买数量')
    image = models.ImageField(upload_to='static/product/%Y/%m', verbose_name='产品图片')

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name
