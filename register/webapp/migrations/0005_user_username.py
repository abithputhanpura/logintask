# Generated by Django 4.0.2 on 2022-02-16 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_alter_user_date_of_birth_alter_user_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='user1', max_length=50),
        ),
    ]