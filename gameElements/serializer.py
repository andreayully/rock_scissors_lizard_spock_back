from rest_framework import serializers

from gameElements.models import Match, GameElement


class GameElementSerializer(serializers.ModelSerializer):
    beats = serializers.SerializerMethodField()

    def get_beats(self, obj):
        try:
            beats = obj.beats.all()
        except GameElement.DoesNotExist:
            return {}
        return [{'id': bt.id, 'name': bt.name} for bt in beats]

    class Meta:
        model = GameElement
        fields = ('id', 'name', 'beats')


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'


class MatchGetSerializer(serializers.ModelSerializer):
    user_1 = serializers.StringRelatedField(many=False)
    user_2 = serializers.StringRelatedField(many=False)
    element_user_1 = serializers.StringRelatedField(many=False)
    element_user_2 = serializers.StringRelatedField(many=False)
    winner = serializers.StringRelatedField(many=False)

    class Meta:
        model = Match
        fields = '__all__'
