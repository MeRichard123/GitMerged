# Generated by Django 3.1 on 2020-08-27 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0034_auto_20200823_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='editor',
            field=models.CharField(blank=True, choices=[('Vim', 'Vim'), ('EMACS', 'EMACS')], default=None, max_length=5, null=True),
        ),
    ]
