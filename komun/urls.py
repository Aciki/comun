
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("api/v1/auth/", include("djoser.urls")),
    # path('api/v1/auth', include('djoser.urls.authtoken')),
    path("api/v1/auth/", include("djoser.urls.jwt")),
    path('admin/', admin.site.urls),
    # path("api/v1/news/", include("apps.news.urls")),
    path( "", include("apps.news.urls",)
        
    ),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
