from rest_framework import generics
from english_words import models
from .serializers import SerTopic


class Topic(generics.ListAPIView):
    serializer_class = SerTopic
    queryset = models.Topics.objects.all()
