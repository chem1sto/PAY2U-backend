# Generated by Django 5.0.3 on 2024-03-18 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='inn',
            field=models.IntegerField(unique=True, verbose_name='ИНН'),
        ),
    ]
