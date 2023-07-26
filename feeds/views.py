# from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from .models import Feed
from .serializers import FeedSerializer

# Create your views here.
# REST API: HTTP METHOD를 호출하는 곳

class AllFeeds(APIView):
    def get(self, request):
        feeds = Feed.objects.all() # 장고 객체
    
        # serializer 장고 객체 -> JSON
        serializer = FeedSerializer(feeds, many=True)
        return Response(serializer.data)

class UserNameFeeds(APIView):
    def get(self, request, username):
        try:
            feeds = Feed.objects.get(id=username)
        except Feed.DoesNotExist:
            raise NotFound

        serializer = FeedSerializer(feeds)
        return Response(serializer.data)