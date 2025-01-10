import uuid
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .emails import send_account_locked_email
from .managers import UserManager

class User(AbstractUser):
    class SecurityQuestions(models.TextChoices):
        MAIDEN_NAME = (
            "maiden_name",
            _("Waht is your mother's maiden name?"),
        )
        FAVORITE_COLOR = (
            "favorite_color",
            _("What is your favorite color?"),
        )
        BIRTH_CITY = (
            "birth_city",
            _("What is the city where you were born?")
        )
        CHILDHOOD_FRIEND = (
            "childhood_friend",
            _("What is the name of your childhood best friend?")
        )
