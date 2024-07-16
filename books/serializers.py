from rest_framework import serializers
from books.models import Book, BookScore


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ['rating']


class BookScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookScore
        fields = '__all__'
        read_only_fields = ['user']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['date_score'] = instance.date_score.strftime('%d/%m/%Y')
        return representation

    def create(self, validated_data):
        user = self.context['request'].user
        book = validated_data['book']
        
        if BookScore.objects.filter(user=user, book=book).exists():
            raise serializers.ValidationError("Book already reviewed!")

        validated_data['user'] = user
        return super().create(validated_data)
