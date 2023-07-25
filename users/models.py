from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    profileImg = models.URLField(blank=True)
    prifileIntroduce = models.CharField(max_length=50)
    followerNum = models.PositiveBigIntegerField(default=0)
    followingNum = models.PositiveBigIntegerField(default=0)
    