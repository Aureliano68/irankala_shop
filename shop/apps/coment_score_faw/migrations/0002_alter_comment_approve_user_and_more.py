# Generated by Django 4.1.4 on 2023-03-04 18:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coment_score_faw', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='approve_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_comment2', to=settings.AUTH_USER_MODEL, verbose_name='کاربر  تایید کننده'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_comment', to=settings.AUTH_USER_MODEL, verbose_name='کاربر نظر دهنده'),
        ),
    ]
