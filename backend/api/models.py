from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=15)
    telegram_chat_id = models.BigIntegerField(default=0, blank=True, null=True, unique=True)


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
    document_photo = models.ImageField(verbose_name="Фото", upload_to="services/photos/", null=True, blank=True)
    phone_number = models.CharField(max_length=15, default="")
    kind_of_activity = models.CharField(verbose_name="Вид деятельности", max_length=150)
    telegram_chat_id = models.BigIntegerField(default=0, blank=True, null=True, unique=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Сервис", null=True)
    verification_code = models.CharField(max_length=6, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}: {self.kind_of_activity}"


class SimpleUserProfile(models.Model):
    tg_username = models.CharField(max_length=150)
    fullname = models.CharField(max_length=255)
    tg_chat_id = models.BigIntegerField()
    phone_number = models.CharField(max_length=15)
    # verification_code = models.CharField(max_length=6, blank=True, null=True)

    def __str__(self):
        return f"{self.fullname}: {self.phone_number}"


class UserRequest(models.Model):
    chat_id = models.BigIntegerField(default=0)
    title = models.CharField(max_length=1000, verbose_name="Заголовок заявки")
    body = models.TextField(verbose_name="Описание заявки")
    username = models.CharField(verbose_name="Username", max_length=255,
                                help_text="Username пользователя бота который оставил заявку")
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING, related_name="requests", verbose_name="Сервис")
    location = models.CharField(verbose_name="Локация", max_length=255)

