# Generated by Django 4.0.4 on 2022-06-16 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0007_alter_profile_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='foto',
            field=models.ImageField(blank=True, height_field=300, upload_to='images', verbose_name='фото', width_field=300),
        ),
    ]