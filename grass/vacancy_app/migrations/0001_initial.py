# Generated by Django 4.0.4 on 2022-06-28 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profile_app', '0015_company_created_at_company_logo_company_updated_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(max_length=150)),
                ('salary_min', models.IntegerField(blank=True, null=True, verbose_name='Минимальная зарплата')),
                ('salary_max', models.IntegerField(blank=True, null=True, verbose_name='Максимальная зарплата')),
                ('location', models.CharField(max_length=150)),
                ('responsibilities', models.TextField()),
                ('requirements', models.TextField()),
                ('working_mode', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_app.company')),
            ],
        ),
    ]