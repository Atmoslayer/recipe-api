# Generated by Django 3.2.15 on 2024-01-26 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='number_of_uses',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество использований'),
        ),
    ]
