from django.shortcuts import render
from rest_framework import generics, filters
# Create your views here.
from users.models import GameUser
from users.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status


class UserCreateListView(generics.ListCreateAPIView):
    """
    GET: user list
    POST: user creation
    """
    queryset = GameUser.objects.all().order_by('-score')
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        score = 0
        if not GameUser.objects.filter(name=data['name']).exists():
            self.perform_create(serializer)
        else:
            score = GameUser.objects.get(name=data['name']).score
        data_response = {
            'name': data['name'],
            'score': score}
        return Response({'data': data_response, 'status': status.HTTP_201_CREATED})
