# Generated by Django 4.1.4 on 2023-02-02 17:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_order_payment_alter_order_register_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='register_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 2, 17, 34, 35, 615504), verbose_name='تاریخ درج سفارش'),
        ),
    ]
