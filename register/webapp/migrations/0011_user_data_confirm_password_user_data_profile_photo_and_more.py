# Generated by Django 4.0.2 on 2022-02-17 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_rename_dob_user_data_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_data',
            name='confirm_password',
            field=models.CharField(default='user1', max_length=100),
        ),
        migrations.AddField(
            model_name='user_data',
            name='profile_photo',
            field=models.ImageField(default='user1', upload_to='profile'),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]