# Generated by Django 5.0.2 on 2024-03-17 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_product_p_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available_from',
            field=models.DateField(default='2024-03-18'),
        ),
        migrations.AddField(
            model_name='product',
            name='available_until',
            field=models.DateField(default='2024-03-18'),
        ),
    ]
