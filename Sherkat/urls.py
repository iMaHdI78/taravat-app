from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import home

urlpatterns = [
    path('', home),
]
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
