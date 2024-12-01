from django.urls import path
from .views import CommandAPIView

urlpatterns = [
    path('', CommandAPIView.as_view(), name='command-api'),
]
