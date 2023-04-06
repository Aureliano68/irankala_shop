# Generated by Django 4.1.4 on 2023-02-01 18:38

import datetime
from django.db import migrations, models
import utilis


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_customer_alter_customeruser_regester_date'),
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
            field=models.DateField(default=datetime.datetime(2023, 2, 1, 18, 38, 31, 842479)),
        ),
    ]