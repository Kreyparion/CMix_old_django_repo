# Generated by Django 3.1.6 on 2021-02-19 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Presta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presta_name', models.CharField(max_length=200)),
                ('presta_date', models.DateTimeField(verbose_name='date of presta')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
