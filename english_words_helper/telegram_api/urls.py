from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = routers.DefaultRouter()
router.register(r'user-words', views.UserWordsSetView, basename='user_words')
router.register(r'words', views.WordsSetView, basename='words')
router.register(r'topics', views.TopicsSetView, basename='topics')
router.register(r'levels', views.LevelsSetView, basename='levels')
router.register(r'verbs', views.VerbsSetView, basename='verbs')

urlpatterns = [
    path('topics/<str:level_name>/', views.DetailTopicsByLevel.as_view()),
    path('', include(router.urls)),
    path('words/level/<str:level_name>/', views.DetailWordsByLevel.as_view()),
    path('words/topic/<str:topic_name>/', views.DetailWordsByTopic.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth-tok/', include('djoser.urls.authtoken')),
    path('drf-auth/', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('token/verify/', TokenVerifyView.as_view()),
]
