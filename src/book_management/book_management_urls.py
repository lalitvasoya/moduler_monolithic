from django.urls import path, include
from rest_framework.routers import DefaultRouter

from src.book_management.views.book_views import CreateBookApiView

router = DefaultRouter()
router.register('book', CreateBookApiView, 'book')

urlpatterns = [
    path('', include(router.urls)),
]
