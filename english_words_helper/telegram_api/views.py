from rest_framework import generics, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from english_words import models
from .serializers import SerTopics, SerLevels, SerWords, SerIrregularVerbs, SerUserWords
from .permissions import IsAdminOrReadOnly


class TopicsSetView(viewsets.ModelViewSet):
    serializer_class = SerTopics
    queryset = models.Topics.objects.all()
    permission_classes = (IsAdminOrReadOnly, )


class LevelsSetView(viewsets.ModelViewSet):
    serializer_class = SerLevels
    queryset = models.Levels.objects.all()
    permission_classes = (IsAdminOrReadOnly, )


class WordsSetView(viewsets.ModelViewSet):
    serializer_class = SerWords
    queryset = models.Words.objects.all()
    permission_classes = (IsAdminOrReadOnly, )


class VerbsSetView(viewsets.ModelViewSet):
    serializer_class = SerIrregularVerbs
    queryset = models.IrregularVerbs.objects.all()
    permission_classes = (IsAdminOrReadOnly, )


class DetailTopicsByLevel(generics.ListAPIView):
    serializer_class = SerTopics

    def get_queryset(self):
        level_name = self.kwargs.get('level_name').upper()
        queryset = models.Topics.objects.all()
        level = get_object_or_404(models.Levels, name=level_name)
        queryset = queryset.filter(level=level)
        return queryset


class DetailWordsByLevel(generics.ListAPIView):
    serializer_class = SerWords

    def get_queryset(self):
        level_name = self.kwargs.get('level_name').upper()
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
            queryset = queryset.filter(topic__name=topic_name)
        return queryset


class UserWordsSetView(viewsets.ModelViewSet):
    queryset = models.UserWords.objects.all()
    serializer_class = SerUserWords
    permission_classes = (IsAuthenticated, )
