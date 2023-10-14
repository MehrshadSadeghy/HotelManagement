from rest_framework import serializers

from .models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            "number",
            "rank",
            "full",
            "price",
            "picture_1",
            "picture_2",
            "picture_3",
            "options",
            "score"
        ]

