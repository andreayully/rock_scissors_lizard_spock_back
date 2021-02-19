from django.shortcuts import render
from rest_framework import generics

# Create your views here.
from gameElements.models import Match, GameElement
from gameElements.serializer import MatchSerializer, GameElementSerializer, MatchGetSerializer
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from users.models import GameUser


class GameElementListView(generics.ListAPIView):
    """
    List and create Match object
    """
    queryset = GameElement.objects.all()
    serializer_class = GameElementSerializer


class InitialMatchCreateView(generics.CreateAPIView):
    """
    Create an empty match
    """
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        user_1, create_1 = GameUser.objects.get_or_create(name=data['user_1'])
        user_2, create_2 = GameUser.objects.get_or_create(name=data['user_2'])
        data['user_1'] = user_1.id
        data['user_2'] = user_2.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user_1=user_1, user_2=user_2)
        self.perform_create(serializer)
        return Response({'data': serializer.data, 'status': status.HTTP_201_CREATED})


class MatchRetriveUpdateView(generics.RetrieveUpdateAPIView):
    """
    List and create Match object
    """
    queryset = Match.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MatchGetSerializer
        else:
            return MatchSerializer

    def update(self, request, *args, **kwargs):
        data = request.data
        data['ts'] = timezone.now()
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=data, partial=True)
        element_1 = GameElement.objects.get(id=data['element_user_1'])
        element_2 = GameElement.objects.get(id=data['element_user_2'])
        serializer.is_valid(raise_exception=True)
        if element_1 in element_2.beats.all():
            winner = instance.user_2
        elif element_2 in element_1.beats.all():
            winner = instance.user_1
        winner.score += 1
        winner.save()
        serializer.save(winner=winner)
        self.perform_update(serializer)
        data_response = {
            'id': instance.id,
            'ts': instance.ts,
            'user_1': instance.user_1.name,
            'user_2': instance.user_2.name,
            'element_user_1': instance.element_user_1.name,
            'element_user_2': instance.element_user_2.name,
            'winner': instance.winner.name,
        }
        return Response({'data': data_response, 'status': status.HTTP_201_CREATED})
