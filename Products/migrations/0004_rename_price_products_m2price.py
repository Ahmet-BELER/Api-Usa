# Generated by Django 4.2 on 2023-05-06 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_alter_products_cashtype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='price',
            new_name='M2price',
        ),
    ]
