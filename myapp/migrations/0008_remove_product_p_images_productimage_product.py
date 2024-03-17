# Generated by Django 5.0.2 on 2024-03-17 19:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_product_p_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='p_images',
        ),
        migrations.AddField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.product'),
        ),
    ]
