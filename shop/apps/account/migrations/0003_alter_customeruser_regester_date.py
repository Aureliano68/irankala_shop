# Generated by Django 4.1.4 on 2022-12-20 21:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_customeruser_regester_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='regester_date',
            field=models.DateField(default=datetime.datetime(2022, 12, 20, 21, 47, 18, 624682)),
        ),
    ]