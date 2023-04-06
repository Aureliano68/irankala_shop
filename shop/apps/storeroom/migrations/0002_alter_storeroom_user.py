# Generated by Django 4.1.4 on 2023-02-22 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('storeroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeroom',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='storeroom_users', to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]
