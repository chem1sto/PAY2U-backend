# Generated by Django 5.0.3 on 2024-03-28 16:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0011_usersubscription_renewal'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersubscription',
            name='access_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='user_access_code', to='subscriptions.accesscode'),
        ),
        migrations.AlterField(
            model_name='usersubscription',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='user_subscription_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
