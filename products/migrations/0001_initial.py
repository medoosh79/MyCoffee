# Generated by Django 3.2 on 2021-04-15 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PrdName', models.CharField(max_length=100, verbose_name=' Name')),
                ('PrdDesc', models.TextField(verbose_name=' Description')),
                ('PrdImage', models.ImageField(blank=True, null=True, upload_to='media', verbose_name='imge/%y/%m/%d/')),
                ('PrdPrice', models.DecimalField(decimal_places=2, max_digits=8, verbose_name=' Price')),
                ('PrdCost', models.DecimalField(decimal_places=2, max_digits=8, verbose_name=' Cost')),
                ('PrdCreated', models.DateTimeField(verbose_name=' Created')),
                ('PrdIsActive', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
    ]
