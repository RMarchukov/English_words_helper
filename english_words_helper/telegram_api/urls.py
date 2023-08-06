from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'words', views.WordsSetView, basename='words')
router.register(r'topics', views.TopicsSetView, basename='topics')
router.register(r'levels', views.LevelsSetView, basename='levels')
router.register(r'verbs', views.VerbsSetView, basename='verbs')

urlpatterns = [
    path('topics/<str:level_name>/', views.DetailTopicsByLevel.as_view()),
    path('', include(router.urls)),
    path('user-words/', views.GetAndPostUserWords.as_view()),
    path('words/level/<str:level_name>/', views.DetailWordsByLevel.as_view()),
    path('words/topic/<str:topic_name>/', views.DetailWordsByTopic.as_view()),
    path('results/', views.Results.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
