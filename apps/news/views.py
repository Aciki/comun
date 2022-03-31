from django.shortcuts import render
import logging

from django.db.models import query
from django.shortcuts import render
from rest_framework import  generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import NewsModel

from .exceptions import NewsNotFound

from .serializers import NewsViewSerializer
# from .models import Food, FoodViews
# from .pagination import FoodPagination
# from .serializers import (FoodCreateSerializer, FoodSerializer,
#                           FoodViewSerializer)

# Create your views here.





class NewsViewsAPIView(generics.ListAPIView):
    serializer_class = NewsViewSerializer
    queryset = NewsModel.objects.all()[:4]


class NewsDetailView(APIView):
    def get(self, request, slug):
        news = NewsModel.objects.get(slug=slug)


        serializer = NewsViewSerializer(news, context={"request": request})

        return Response(serializer.data, status=status.HTTP_200_OK)