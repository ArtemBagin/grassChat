# Generated by Django 4.0.4 on 2022-06-28 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacancy_app',
            old_name='company_name',
            new_name='company',
        ),
    ]