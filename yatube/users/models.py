from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    profile_picture = models.ImageField(
        "Фото профиля",
        upload_to="users/",
        default="users/default_profile_picture.jpg",
        blank=True,
        null=True,
        help_text="Загрузите фото профиля",
    )
