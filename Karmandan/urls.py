from django.urls import path
from .views import Karmandan, KarmandView

urlpatterns = [
    path('', KarmandView.as_view()),

]