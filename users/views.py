from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from .models import User
from .serializers import UserSerializer

# Create your views here.
class Users(APIView):
    def get(self, request): #사용자 데이터를 조회

        users = User.objects.all()

        serializer = UserSerializer(users, many =True)

        return Response(serializer.data)

class UserDetail(APIView):
    def get(self, request, user_id):


        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise NotFound

        serializer = UserSerializer(user)
        print(serializer)

        return Response(serializer.data)
