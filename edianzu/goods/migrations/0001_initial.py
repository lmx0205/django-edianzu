# Generated by Django 2.1.2 on 2018-11-14 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='租金')),
                ('cost_price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='押金')),
                ('details', models.TextField(verbose_name='详情')),
                ('num', models.IntegerField(verbose_name='购买数量')),
                ('image', models.ImageField(upload_to='static/product/%Y/%m', verbose_name='产品图片')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.UserProfile', verbose_name='用户')),
            ],
            options={
                'verbose_name': '购物车',
                'verbose_name_plural': '购物车',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hello', models.CharField(max_length=500, verbose_name='产品单位')),
                ('name', models.CharField(max_length=500, verbose_name='产品类别')),
                ('unit', models.CharField(max_length=100, verbose_name='产品品牌')),
                ('keywords', models.CharField(max_length=200, verbose_name='关键词')),
                ('image', models.ImageField(upload_to='static/product/%Y/%m', verbose_name='产品图片')),
                ('barcode', models.CharField(max_length=100, verbose_name='配置')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='押金')),
                ('market_price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='随租随还')),
                ('cost_price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='租完即送')),
                ('count', models.IntegerField(default=0, verbose_name='库存')),
                ('sales_count', models.IntegerField(default=0, verbose_name='销量')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('status', models.IntegerField(choices=[(0, '下架'), (1, '上架')], verbose_name='状态')),
                ('details', models.TextField(verbose_name='详情')),
            ],
            options={
                'verbose_name': '产品',
                'verbose_name_plural': '产品',
            },
        ),
    ]
