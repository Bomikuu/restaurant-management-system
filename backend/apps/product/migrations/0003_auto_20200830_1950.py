# Generated by Django 3.0.8 on 2020-08-30 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='products/', verbose_name='Product Image'),
        ),
    ]