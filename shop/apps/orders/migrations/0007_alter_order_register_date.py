# Generated by Django 4.1.4 on 2023-02-10 08:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_order_register_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='register_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 10, 8, 11, 26, 920920), verbose_name='تاریخ درج سفارش'),
        ),
    ]
