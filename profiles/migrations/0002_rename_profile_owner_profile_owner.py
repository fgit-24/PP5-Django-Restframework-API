# Generated by Django 4.2 on 2024-04-22 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_owner',
            new_name='owner',
        ),
    ]
