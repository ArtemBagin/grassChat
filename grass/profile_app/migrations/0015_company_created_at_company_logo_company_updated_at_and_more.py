# Generated by Django 4.0.4 on 2022-06-19 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import profile_app.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profile_app', '0014_profile_created_at_profile_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, upload_to=profile_app.models.user_directory_path, verbose_name='Лого'),
        ),
        migrations.AddField(
            model_name='company',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='about_company',
            field=models.TextField(blank=True, verbose_name='О компании'),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Название компании'),
        ),
        migrations.AlterField(
            model_name='company',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile_company', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skills',
            field=models.TextField(blank=True, max_length=2000, verbose_name='Навыки'),
        ),
    ]