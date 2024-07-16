from rest_framework import serializers
from games.models import Game, GameScore


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'
        read_only_fields = ['rating']


class GameScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameScore
        fields = '__all__'
        read_only_fields = ['user']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['date_score'] = instance.date_score.strftime('%d/%m/%Y')
        return representation

    def create(self, validated_data):
        user = self.context['request'].user
        game = validated_data['game']
        
        if GameScore.objects.filter(user=user, game=game).exists():
            raise serializers.ValidationError("Game already reviewed!")

        validated_data['user'] = user
        return super().create(validated_data)
