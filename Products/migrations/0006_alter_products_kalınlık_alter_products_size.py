# Generated by Django 4.2 on 2023-05-10 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0005_rename_m2price_products_m2price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='kalınlık',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='size',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
