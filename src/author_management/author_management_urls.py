from django.urls import path, include
from rest_framework.routers import DefaultRouter

from src.author_management.views.author_views import CreateAuthorApiView

router = DefaultRouter()
router.register('author', CreateAuthorApiView, 'author')

urlpatterns = [
    path('', include(router.urls)),
]
