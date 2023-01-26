from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from social_django.models import UserSocialAuth


import uuid


class User(AbstractBaseUser):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    social_auth = models.OneToOneField(UserSocialAuth, on_delete=models.CASCADE, null=True)


