# Generated by Django 4.0.4 on 2023-08-08 13:00

from django.db import migrations, models
import profile_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0018_alter_profile_gender_alter_profile_relocate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, height_field=100, upload_to=profile_app.models.user_directory_path, verbose_name='фото', width_field=100),
        ),
    ]