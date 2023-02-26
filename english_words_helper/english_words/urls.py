from django.urls import path
from . import views

urlpatterns = [
    path('', views.Level.as_view(), name='level'),
    path('topic/<str:my_arg>/', views.Topic.as_view(), name='topic'),
    path('word/<str:my_arg>/', views.Word.as_view(), name='word')
]
