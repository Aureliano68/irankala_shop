# Generated by Django 4.1.4 on 2022-12-29 01:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_customeruser_regester_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='regester_date',
            field=models.DateField(default=datetime.datetime(2022, 12, 29, 1, 14, 12, 898136)),
        ),
    ]
