from rest_framework import serializers

from users.models import GameUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameUser
        fields = '__all__'
