# Generated by Django 4.0.4 on 2023-08-10 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0024_rename_exp_profile_expjob_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='inn',
            field=models.BigIntegerField(blank=True, verbose_name='Инн организации'),
        ),
        migrations.AlterField(
            model_name='expjob',
            name='at_now_time',
            field=models.BooleanField(verbose_name='по настоящее время'),
        ),
    ]
