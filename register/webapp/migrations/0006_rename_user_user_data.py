# Generated by Django 4.0.2 on 2022-02-16 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_user_username'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='User_data',
        ),
    ]
