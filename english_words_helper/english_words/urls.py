from django.urls import path
from . import views

urlpatterns = [
    path('', views.Level.as_view(), name='level'),
    path('topic/<str:my_arg>/', views.Topic.as_view(), name='topic'),
    path('word/<str:my_arg>/', views.Word.as_view(), name='word'),
    path('irregularverb/', views.IrregularVerb.as_view(), name='verb'),
    path('translate/<str:my_arg>/', views.FromEnglish.as_view(), name='translate'),
    path('check_translation/<str:my_arg>/', views.CheckTranslationView.as_view(), name='check_translation'),
]
