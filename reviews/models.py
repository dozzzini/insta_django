from django.db import models
from commons.models import CommonModel

# Create your models here.

class Review(CommonModel):
    rcaption = models.CharField(max_length=50) # 내용