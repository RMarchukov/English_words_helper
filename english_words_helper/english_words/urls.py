from django.urls import path
from . import views


urlpatterns = [
    path('word/<str:my_arg>/', views.Word.as_view(), name='word'),
    path('irregularverb/', views.IrregularVerb.as_view(), name='verb'),
    path('translate/<str:my_arg>/', views.FromEnglish.as_view(), name='translate'),
    path('check_translation/<str:my_arg>/', views.CheckTranslationView.as_view(), name='check_translation'),
    path('add_word/', views.AddWord.as_view(), name='add_word'),
    path('show_words/', views.ShowWords.as_view(), name='show_words'),
    path('show_tests/', views.ShowTests.as_view(), name='show_tests'),
    path('', views.BaseView.as_view(), name='base'),
    path('translate/', views.translate, name='types'),
    path('token/', views.UserToken.as_view(), name='token'),
    path('api-info/', views.get_endpoints, name='api'),
]
