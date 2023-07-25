from django.db import models

# Create your models here.

class CommonModel(models.Model):

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True) #수정되면 같이 변경


    class Meta: 
        abstract = True