from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("src.book_management.book_management_urls")),
    path("", include("src.author_management.author_management_urls")),
    path('api-auth/', include('rest_framework.urls'))
]
