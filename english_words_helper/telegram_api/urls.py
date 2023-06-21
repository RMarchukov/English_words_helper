from django.urls import path
from . import views


urlpatterns = [
    path('topics/', views.Topics.as_view(), name='topicsAPI'),
    path('topics/<str:my_arg>/', views.DetailTopicsByLevel.as_view(), name='detail_topics'),
    path('levels/', views.Levels.as_view(), name='levelsAPI'),
    path('words/', views.Words.as_view(), name='wordsAPI'),
    path('words/by-level/<str:level_name>/', views.DetailWordsByLevel.as_view(), name='detail_words_by_level'),
    path('words/by-topic/<str:topic_name>/', views.DetailWordsByTopic.as_view(), name='detail_words_by_topic'),
]
