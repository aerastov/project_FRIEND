from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=16, verbose_name='Телефон')  # +79167003020
    birth = models.DateField(verbose_name='Дата рождения')  # 2000-07-28
    tg = models.CharField(max_length=32, blank=True, verbose_name='Тег')  # @Rubella19

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'