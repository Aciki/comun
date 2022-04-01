
from rest_framework import serializers

from .models import NewsModel


class NewsViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = (
            "id",
            "title",
            # "get_absolute_url",
            "descripton",
            
            "get_image",
            "get_thumbnail"
        )