# Generated by Django 3.1 on 2020-08-21 11:55

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_profile_tech_stacks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='tech_stacks',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'PHP'), (2, 'Ruby'), (3, 'Java'), (4, 'Python'), (5, 'Javascript')], max_length=9, null=True),
        ),
    ]
