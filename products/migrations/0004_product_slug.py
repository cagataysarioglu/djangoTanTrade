# Generated by Django 3.1.5 on 2021-01-26 07:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210125_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=datetime.date.today, verbose_name='Bulunak'),
            preserve_default=False,
        ),
    ]
