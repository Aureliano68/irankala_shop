# Generated by Django 4.1.4 on 2023-02-01 18:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='discount',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='تخفیف روی فاکتور'),
        ),
        migrations.AlterField(
            model_name='order',
            name='register_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 1, 18, 38, 31, 859480), verbose_name='تاریخ درج سفارش'),
        ),
    ]
