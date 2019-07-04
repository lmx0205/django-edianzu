from django.contrib import admin
from .models import Goods,Cart

@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    pass

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass




