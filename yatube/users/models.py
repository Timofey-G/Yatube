from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    profile_picture = models.ImageField(
        "Фото профиля",
        upload_to="users/",
        blank=True,
        help_text="Загрузите фото профиля",
    )
