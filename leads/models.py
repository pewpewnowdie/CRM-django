from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username

class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    orgamisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username

def post_save_user_created(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_save_user_created, sender=User)