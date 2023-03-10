from django.shortcuts import render
from django.views.generic import ListView, FormView
from .models import Words, Levels, Topics, IrregularVerbs, UserWords, UserTests
from random import choice
from django.views import View
from .forms import UserWordsForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


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
    template_name = 'words/verbs.html'
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
        word_id = request.POST.get('word_id')
        translation = request.POST.get('translation')
        one = request.POST.get('one')
        two = request.POST.get('two')
        three = request.POST.get('three')
        four = request.POST.get('four')

        word = Words.objects.get(id=word_id)

        if request.user.is_authenticated:
            user = self.request.user
            try:
                user_tests = UserTests.objects.get(user=user)
            except UserTests.DoesNotExist:
                user_tests = UserTests(user=user, all_test=0, true_test=0, false_test=0)
            user_tests.all_test += 1

        if one == word.in_english or two == word.in_english or three == word.in_english or four == word.in_english or \
                translation == word.in_english:
            result = "Вірно!"
            if request.user.is_authenticated:
                user_tests.true_test += 1
        elif one == word.in_ukrainian or two == word.in_ukrainian or three == word.in_ukrainian or \
                four == word.in_ukrainian or translation == word.in_ukrainian:
            result = "Вірно!"
            if request.user.is_authenticated:
                user_tests.true_test += 1
        else:
            result = "Неправильно!"
            if request.user.is_authenticated:
                user_tests.false_test += 1

        if request.user.is_authenticated:
            user_tests.save()

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


class AddWord(LoginRequiredMixin, FormView):
    template_name = 'words/add_word.html'
    form_class = UserWordsForm
    success_url = reverse_lazy('level')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        user_id = self.request.user.id

        if user_id is not None:
            form.instance.user_id = user_id
        form.save()
        return super().form_valid(form)


class ShowWords(LoginRequiredMixin, ListView):
    template_name = 'words/show_words.html'
    model = UserWords
    context_object_name = 'user_words'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return UserWords.objects.filter(user=self.request.user)


class ShowTests(LoginRequiredMixin, ListView):
    template_name = 'words/show_tests.html'
    model = UserTests
    context_object_name = 'user_tests'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        queryset = UserTests.objects.filter(user=self.request.user)
        user_test = queryset[0]
        return user_test


def main(request):
    return render(request, 'words/main.html')


def translate(request):
    types = ['test', 'eng-test', 'choice', 'eng-choice']
    context = {'types': types}
    return render(request, 'words/translate.html', context)
