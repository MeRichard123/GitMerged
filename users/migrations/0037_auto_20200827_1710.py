# Generated by Django 3.1 on 2020-08-27 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0036_auto_20200827_1709'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='operating_system',
            new_name='os',
        ),
    ]