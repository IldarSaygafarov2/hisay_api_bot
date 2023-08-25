from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class UserProfile(AbstractUser):
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=15)
    telegram_chat_id = models.BigIntegerField(default=0, blank=True, null=True)


class Service(models.Model):
    name = models.CharField(verbose_name="Сервис", max_length=150)

    def __str__(self):
        return self.name


class ServiceHashtag(models.Model):
    name = models.CharField(verbose_name="Хештег", max_length=255)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="services")

    def __str__(self):
        return self.name


class ServiceProfile(models.Model):
    first_name = models.CharField(verbose_name="Имя", max_length=150)
    last_name = models.CharField(verbose_name="Фамилия", max_length=150)
    surname = models.CharField(verbose_name="Отчество", max_length=150)
    document_photo = models.ImageField(verbose_name="Фото", upload_to="services/photos/")
    kind_of_activity = models.CharField(verbose_name="Вид деятельности", max_length=150)
    telegram_chat_id = models.BigIntegerField(default=0, blank=True, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Сервис", null=True)
