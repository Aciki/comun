
from rest_framework import serializers

from .models import NewsModel


class NewsViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        exclude = ["created_at", ]