# Generated by Django 4.0.4 on 2022-06-16 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0006_profile_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, default='04.03.2000', null=True, verbose_name='Дата рождения'),
        ),
    ]