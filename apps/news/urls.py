

from django.urls import path

from . import views

urlpatterns = [
    path("all/", views.NewsViewsAPIView.as_view(), name="all-news"),
    path(
            "details/<slug:slug>/",
            views.NewsDetailView.as_view(),
            name="news-details",
        ),
        ]