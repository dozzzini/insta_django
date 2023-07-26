from django.db import models
from commons.models import CommonModel

# Create your models here.

class Feed(CommonModel):
    caption = models.CharField(max_length=120) # 게시글 내용
    contentImg = models.URLField(blank=True) # 게시글 이미지
    likesNum = models.PositiveBigIntegerField(default=0)


users = models.ForeignKey(
    "users.User",
    on_delete = models.CASCADE, # 유저가 삭제됐을 때 게시글도 삭제한다. 
    # on_delete = models.SET_NULL, # 유저가 삭제됐을 때 게시글은 가만히 둔다. 
)