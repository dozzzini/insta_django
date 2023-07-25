from django.db import models
from commons.models import CommonModel

# Create your models here.

class Feed(CommonModel):
    caption = models.CharField(max_length=120) # 게시글 내용
    contentImg = models.URLField(blank=True) # 게시글 이미지
    likesNum = models.PositiveBigIntegerField(default=0)
