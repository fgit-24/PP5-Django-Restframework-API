# Generated by Django 4.2 on 2024-04-22 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_owner',
            new_name='owner',
        ),
    ]
