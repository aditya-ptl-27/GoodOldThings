# Generated by Django 5.0.2 on 2024-03-17 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_remove_product_p_images_productimage_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='p_description',
            field=models.TextField(),
        ),
    ]
