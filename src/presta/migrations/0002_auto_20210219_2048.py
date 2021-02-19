# Generated by Django 3.1.6 on 2021-02-19 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='presta',
            name='presta_respo',
            field=models.CharField(default='Hola', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='presta',
            name='presta_respo_mail',
            field=models.EmailField(default='admin@example.com', max_length=254, verbose_name='email respo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='presta',
            name='presta_type',
            field=models.CharField(choices=[('FP', 'FP'), ('GS', 'Grande Soirée'), ('SC', 'Soirée Chill')], default='FP', max_length=3),
            preserve_default=False,
        ),
    ]
