from django.urls import path
from . import views


urlpatterns = [
    path('topic/', views.Topic.as_view(), name='topicAPI'),
]
