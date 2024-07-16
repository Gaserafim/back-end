from rest_framework import serializers
from hqs.models import HQ, HQScore


class HQSerializer(serializers.ModelSerializer):
    class Meta:
        model = HQ
        fields = "__all__"
        read_only_fields = ["rating"]


class HQScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = HQScore
        fields = "__all__"
        read_only_fields = ["user"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["date_score"] = instance.date_score.strftime("%d/%m/%Y")
        return representation

    def create(self, validated_data):
        user = self.context["request"].user
        hq = validated_data["hq"]

        if HQScore.objects.filter(user=user, hq=hq).exists():
            raise serializers.ValidationError("HQ already reviewed!")

        validated_data["user"] = user
        return super().create(validated_data)
