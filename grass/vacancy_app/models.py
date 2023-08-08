from django.db import models
from profile_app.models import Company


# Create your models here.
class Vacancy(models.Model):
    class Meta:
        verbose_name_plural = "vacancies"

    job_name = models.CharField(max_length=150, verbose_name="Название вакансии")
    salary_min = models.IntegerField(verbose_name="Минимальная зарплата", blank=True, null=True)
    salary_max = models.IntegerField(verbose_name="Максимальная зарплата", blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    location = models.CharField(max_length=150, verbose_name="Место положения")
    responsibilities = models.TextField(verbose_name="Возможности")
    requirements = models.TextField(verbose_name="Требования")
    work_experience = models.IntegerField(verbose_name="Опыт работы", blank=True, null=True)


    #удаленно, стажировка, полная занятость, частичная занятость
    working_mode = models.CharField(max_length=200, verbose_name="Тип занятости")

    #key_skills = models.ForeignKey()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return f'/vacancy/{self.pk}'

    def __str__(self):
        return self.job_name

    def get_work_exp_end(self):
        if self.work_experience == 1:
            return f'от 1 года'
        else:
            return f'от {self.work_experience} лет'


# class Skill(models.Model):
#     title = None
#     slug = None

