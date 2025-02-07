from rest_framework import serializers


class TextSerializer(serializers.Serializer):
    text = serializers.CharField(required=True, max_length=999)
