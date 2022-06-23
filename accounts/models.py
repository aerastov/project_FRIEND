from django.db import models
from django.contrib.auth.models import User
# from django.core.validators import RegexValidator

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.OneToOneField
    # phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    # phone = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True)  # +79167003020
    phone = models.CharField(max_length=16, unique=True, verbose_name='Телефон')  # +79167003020
    birth = models.DateField(blank=True, verbose_name='Дата рождения')  # 2000-07-28
    tg = models.CharField(max_length=32, blank=True, verbose_name='Тег')  # @Rubella19

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'