# Generated by Django 3.0.4 on 2020-04-23 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='services',
            old_name='updated',
            new_name='update',
        ),
    ]
