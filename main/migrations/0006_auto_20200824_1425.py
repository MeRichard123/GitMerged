# Generated by Django 3.1 on 2020-08-24 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200824_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='status',
            field=models.CharField(choices=[(1, 'Read'), (2, 'Unread')], default=1, max_length=100, null=True),
        ),
    ]
