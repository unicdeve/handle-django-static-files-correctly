from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django_assets.storage_backends import UserAvatarStorage
class User(AbstractUser):
    first_name = models.CharField(_('first name'), max_length=150)
    last_name = models.CharField(_('last name'), max_length=150)
    email = models.EmailField(_('email address'), unique=True)
    avatar = models.ImageField(_('avatar'), upload_to='avatars/', null=True, blank=True, storage=UserAvatarStorage)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email
