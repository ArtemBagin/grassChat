# Generated by Django 4.0.4 on 2023-07-27 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0008_alter_education_profile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='city',
            field=models.CharField(blank=True, max_length=50, verbose_name='Город регистрации компании'),
        ),
        migrations.AddField(
            model_name='company',
            name='count_of_employees',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Количество работников'),
        ),
        migrations.AddField(
            model_name='company',
            name='inn',
            field=models.BigIntegerField(blank=True, default=9999999999, verbose_name='Инн организации'),
        ),
    ]