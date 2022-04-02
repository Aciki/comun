
from rest_framework import serializers

from .models import NewsModel


class NewsViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = (
            "id",
            "title",
            "get_absolute_url",
            "descripton",
            "created_at",
            
            "get_image",
            "get_thumbnail"
        )