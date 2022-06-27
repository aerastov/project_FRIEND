from django.contrib.auth.base_user import BaseUserManager
from accounts.models import Profile
from django.contrib.auth.models import User
from django.db import models

class UserManager(models.Manager):


    def create(self, username, email, is_premium_member=False, has_support_contract=False):
        user = User(username=username, email=email)
        user.save()
        profile = Profile(
            user=user,
        )
        profile.save()
        return user