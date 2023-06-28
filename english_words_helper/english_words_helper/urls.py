from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('english_words.urls')),
    path('users/', include('users.urls')),
    path('api/', include('telegram_api.urls')),
]
