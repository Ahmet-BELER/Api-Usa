# Generated by Django 4.2 on 2023-05-10 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0006_alter_products_kalınlık_alter_products_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
