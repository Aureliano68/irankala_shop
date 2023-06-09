# Generated by Django 4.1.4 on 2023-02-21 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0012_alter_brand_brand_image_and_more'),
        ('account', '0014_alter_customer_image_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreroomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storeroom_type_title', models.CharField(max_length=50, verbose_name='نوع انبار')),
            ],
            options={
                'verbose_name': 'نوع انبار',
                'verbose_name_plural': 'انبار روش انبار',
                'db_table': 'storeroomtype',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='StoreRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField(verbose_name='تعداد')),
                ('price', models.PositiveIntegerField(blank=True, null=True, verbose_name='قیمت')),
                ('register', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='storeroom_products', to='product.product', verbose_name='کالا')),
                ('storeroom_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='storerooms', to='storeroom.storeroomtype', verbose_name='انبار')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='storeroom_users', to='account.customer', verbose_name='کاربر')),
            ],
            options={
                'verbose_name': ' انبار',
                'verbose_name_plural': 'انبارها',
                'db_table': 'storeroom',
                'managed': True,
            },
        ),
    ]
