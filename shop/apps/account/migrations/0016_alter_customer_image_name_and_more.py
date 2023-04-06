# Generated by Django 4.1.4 on 2023-03-04 12:44

import datetime
from django.db import migrations, models
import utilis


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_alter_customer_image_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image_name',
            field=models.ImageField(upload_to=utilis.FileUpload.imageupload, verbose_name='تصویر پروفایل'),
        ),
        migrations.AlterField(
            model_name='customeruser',
            name='regester_date',
            field=models.DateField(default=datetime.datetime(2023, 3, 4, 12, 44, 0, 582330)),
        ),
    ]
