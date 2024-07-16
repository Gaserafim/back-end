from rest_framework import serializers
from series.models import Series, SerieScore


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = '__all__'


class SerieScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = SerieScore
        fields = '__all__'
        read_only_fields = ['user']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['date_score'] = instance.date_score.strftime('%d/%m/%Y')
        return representation

    def create(self, validated_data):
        user = self.context['request'].user
        serie = validated_data['serie']
        
        if SerieScore.objects.filter(user=user, serie=serie).exists():
            raise serializers.ValidationError("Serie already reviewed!")

        validated_data['user'] = user
        return super().create(validated_data)