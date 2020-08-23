# Generated by Django 3.1 on 2020-08-23 15:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0033_profile_blocked_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='blocked_by',
            field=models.ManyToManyField(blank=True, related_name='blocked', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='likeability',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]