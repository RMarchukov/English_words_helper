from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from english_words import models
from .serializers import SerTopics, SerLevels, SerWords, SerIrregularVerbs


class Topics(generics.ListAPIView):
    serializer_class = SerTopics
    queryset = models.Topics.objects.all()


class Levels(generics.ListAPIView):
    serializer_class = SerLevels
    queryset = models.Levels.objects.all()


class Words(generics.ListAPIView):
    serializer_class = SerWords
    queryset = models.Words.objects.all()
    permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication, )


class DetailTopicsByLevel(generics.ListAPIView):
    serializer_class = SerTopics

    def get_queryset(self):
        queryset = models.Topics.objects.all()
        my_arg = self.kwargs.get('my_arg', None)
        if my_arg == 'verbs':
            level = get_object_or_404(models.Levels, name=my_arg)
            if level:
                queryset = queryset.filter(level=level)
        return queryset


class DetailWordsByLevel(generics.ListAPIView):
    def get_serializer_class(self):
        level_name = self.kwargs.get('level_name')
        if level_name == 'verbs':
            serializer_class = SerIrregularVerbs
        else:
            serializer_class = SerWords
        return serializer_class

    def get_queryset(self):
        level_name = self.kwargs.get('level_name').upper()
        if level_name == 'VERBS':
            queryset = models.IrregularVerbs.objects.all()
        else:
            queryset = models.Words.objects.all()
            level = get_object_or_404(models.Levels, name=level_name)
            queryset = queryset.filter(topic__level=level)
        return queryset


class DetailWordsByTopic(generics.ListAPIView):
    serializer_class = SerWords

    def get_queryset(self):
        queryset = models.Words.objects.all()
        topic_name = self.kwargs.get('topic_name').lower()
        if topic_name:
            topic = get_object_or_404(models.Topics, name=topic_name)
            queryset = queryset.filter(topic=topic)
        return queryset
