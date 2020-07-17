from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

#extend the AbstractUser model

class User(AbstractUser):
    # redefining the email and username fields, so we set  the unique paramaters as true
    # and that the username field can be blank, so username won't be required
    username = models.CharField(blank=True, null=True, max_length=255)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    # what fields must be entered when creating a new user
    # We added username to required fields even though it can be blank, otherwise Django complains
    #when creating superusers
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)

class UserProfile(models.Model):


    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=255, unique=True)
