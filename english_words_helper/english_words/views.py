from django.shortcuts import render
from django.views.generic import ListView
from .models import Words, Levels, Topics, IrregularVerbs
from random import choice
from django.views import View


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


class IrregularVerb(ListView):
    template_name = 'words/word.html'
    queryset = IrregularVerbs.objects.all()


class FromEnglish(View):

    def get(self, request, my_arg):
        my_arg = self.kwargs.get('my_arg', None)
        all_words = Words.objects.all()
        random_word = choice(all_words)
        one = choice(all_words)
        two = choice(all_words)
        three = choice(all_words)
        four = choice(all_words)

        context = {'word': random_word, 'one': one, 'two': two, 'three': three, 'four': four}
        if my_arg == 'test':
            return render(request, 'words/test.html', context)
        if my_arg == 'choice':
            return render(request, 'words/choice.html', context)
        if my_arg == 'eng-test':
            return render(request, 'words/test_english.html', context)
        if my_arg == 'eng-choice':
            return render(request, 'words/choice_english.html', context)


class CheckTranslationView(View):
    def post(self, request, my_arg):
        # Отримуємо дані з форми
        word_id = request.POST.get('word_id')
        translation = request.POST.get('translation')
        one = request.POST.get('one')
        two = request.POST.get('two')
        three = request.POST.get('three')
        four = request.POST.get('four')

        # Знаходимо слово у базі даних
        word = Words.objects.get(id=word_id)

        # Перевіряємо переклад
        if one == word.in_english or two == word.in_english or three == word.in_english or four == word.in_english or \
                translation == word.in_english:
            result = "Вірно!"
        elif one == word.in_ukrainian or two == word.in_ukrainian or three == word.in_ukrainian or \
                four == word.in_ukrainian or translation == word.in_ukrainian:
            result = "Вірно!"
        else:
            result = "Неправильно!"

        # Передаємо результат у шаблон та повертаємо його
        context = {'result': result, 'word': word, 'translation': translation}
        my_arg = self.kwargs.get('my_arg', None)
        if my_arg == 'test':
            return render(request, 'words/check_translation.html', context)
        if my_arg == 'choice':
            return render(request, 'words/check_translation_choice.html', context)
        if my_arg == 'eng-test':
            return render(request, 'words/check_translation_english.html', context)
        if my_arg == 'eng-choice':
            return render(request, 'words/check_translation_choice_english.html', context)
