# Generated by Django 4.1.4 on 2023-02-02 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cupon',
            name='end_date',
            field=models.DateTimeField(verbose_name='تاریخ پایان'),
        ),
        migrations.AlterField(
            model_name='cupon',
            name='start_date',
            field=models.DateTimeField(verbose_name='تاریخ شروع'),
        ),
        migrations.AlterField(
            model_name='cuponbasket',
            name='end_date',
            field=models.DateTimeField(verbose_name='تاریخ پایان'),
        ),
        migrations.AlterField(
            model_name='cuponbasket',
            name='start_date',
            field=models.DateTimeField(verbose_name='تاریخ شروع'),
        ),
    ]
