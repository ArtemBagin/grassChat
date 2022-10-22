# Generated by Django 4.0.4 on 2022-06-17 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0009_alter_profile_foto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='foto',
            new_name='photo',
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
    ]