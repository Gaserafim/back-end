from rest_framework import serializers
from movies.models import Movie, MovieScore


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class MovieScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieScore
        fields = '__all__'
        read_only_fields = ['user']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['date_score'] = instance.date_score.strftime('%d/%m/%Y')
        return representation

    def create(self, validated_data):
        user = self.context['request'].user
        movie = validated_data['movie']
        
        if MovieScore.objects.filter(user=user, movie=movie).exists():
            raise serializers.ValidationError("Movie already reviewed!")

        validated_data['user'] = user
        return super().create(validated_data)
