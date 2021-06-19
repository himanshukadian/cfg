from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group

User = settings.AUTH_USER_MODEL


class Mentor(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='mentor')
    bio = models.TextField(blank=True, max_length=100, default="")

    def __str__(self):
        return f'{self.user.username}'

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @property
    def username(self):
        return self.user.username

    class Meta:
        db_table = 'mentor'
