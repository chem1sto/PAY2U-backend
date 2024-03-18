# Generated by Django 5.0.3 on 2024-03-18 12:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('inn', models.IntegerField(max_length=12, unique=True, verbose_name='ИНН')),
            ],
            options={
                'verbose_name': 'Банк',
                'verbose_name_plural': 'Банки',
            },
        ),
        migrations.CreateModel(
            name='BankUser',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('bank_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bank_user', to='payments.bank')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bank_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Пользователь банка',
                'verbose_name_plural': 'Пользователи банков',
            },
        ),
    ]