from django.urls import path
from .views import AllFeeds, UserNameFeeds

urlpatterns=[
    path("", AllFeeds.as_view()), # 전체 게시글을 가져옴

    path("<str:username>", UserNameFeeds.as_view()) # 특정 user가 작성한  url 을 가져옴
]

# api/v1/feeds -> 전체 게시글을 불러오는 API
# api/v1/feeds/<username> -> 특정 유저의 게시글만 불러오는 API

