# Generated by Django 4.1.4 on 2023-02-02 12:13

from django.db import migrations, models
import utilis


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_brand_brand_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand_image',
            field=models.ImageField(upload_to=utilis.FileUpload.imageupload, verbose_name='تصویر برند'),
        ),
        migrations.AlterField(
            model_name='galeryproduct',
            name='product_image',
            field=models.ImageField(upload_to=utilis.FileUpload.imageupload, verbose_name='تصاویر کالا'),
        ),
        migrations.AlterField(
            model_name='groupproduct',
            name='grouppro_image',
            field=models.ImageField(upload_to=utilis.FileUpload.imageupload, verbose_name='تصویر گروه کالا'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(upload_to=utilis.FileUpload.imageupload, verbose_name='تصویر  کالا'),
        ),
    ]
