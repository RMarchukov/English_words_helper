from django.urls import path
from . import views

urlpatterns = [
    path('level/', views.Level.as_view(), name='level'),
    path('topic/<str:my_arg>/', views.Topic.as_view(), name='topic'),
    path('word/<str:my_arg>/', views.Word.as_view(), name='word'),
    path('irregularverb/', views.IrregularVerb.as_view(), name='verb'),
    path('translate/<str:my_arg>/', views.FromEnglish.as_view(), name='translate'),
    path('check_translation/<str:my_arg>/', views.CheckTranslationView.as_view(), name='check_translation'),
    path('add_word/', views.AddWord.as_view(), name='add_word'),
    path('show_words/', views.ShowWords.as_view(), name='show_words'),
    path('show_tests/', views.ShowTests.as_view(), name='show_tests'),
    path('', views.main, name='main'),
    path('translate/', views.translate, name='types')
]
