# Generated by Django 3.1 on 2020-08-22 16:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0026_auto_20200822_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='likeability',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]