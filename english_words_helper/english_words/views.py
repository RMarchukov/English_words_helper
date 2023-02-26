from django.shortcuts import render
from django.views.generic import ListView
from .models import Words, Levels, Topics


class Level(ListView):
    template_name = 'words/level.html'
    queryset = Levels.objects.all()


class Topic(ListView):
    template_name = 'words/topic.html'
    model = Topics

    def get_queryset(self):
        queryset = super().get_queryset()
        my_arg = self.kwargs.get('my_arg', None)
        if my_arg:
            queryset = queryset.filter(level_id=my_arg)
        return queryset


class Word(ListView):
    template_name = 'words/word.html'
    model = Words

    def get_queryset(self):
        queryset = super().get_queryset()
        my_arg = self.kwargs.get('my_arg', None)
        if my_arg:
            queryset = queryset.filter(topic_id=my_arg)
        return queryset
