# Generated by Django 3.1.6 on 2021-04-17 09:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presta', '0006_auto_20210417_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presta',
            name='presta_date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='date of presta'),
        ),
    ]
