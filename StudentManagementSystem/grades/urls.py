# grades/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GradeViewSet

router = DefaultRouter()
router.register(r'grades', GradeViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),  # Добавляем версию API для лучшей управляемости
]