# Generated by Django 3.2 on 2021-04-15 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PrdDescountPrice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Descount Price'),
            preserve_default=False,
        ),
    ]
