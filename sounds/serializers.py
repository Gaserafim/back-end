from rest_framework import serializers
from sounds.models import Sound, SoundScore


class SoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sound
        fields = '__all__'


class SoundScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoundScore
        fields = '__all__'
        read_only_fields = ['user']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['date_score'] = instance.date_score.strftime('%d/%m/%Y')
        return representation

    def create(self, validated_data):
        user = self.context['request'].user
        sound = validated_data['sound']
        
        if SoundScore.objects.filter(user=user, sound=sound).exists():
            raise serializers.ValidationError("Sound already reviewed!")

        validated_data['user'] = user
        return super().create(validated_data)
