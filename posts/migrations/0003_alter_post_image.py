# Generated by Django 4.2 on 2024-10-22 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_rename_post_owner_post_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='../default_post_hy4tc9', upload_to='images/'),
        ),
    ]
