from django.views.generic import ListView, FormView
from djoser.conf import User

from .models import Words, Levels, Topics, IrregularVerbs, UserWords, UserTests
from random import choice
from django.views import View
from .forms import UserWordsForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from django.core.exceptions import ObjectDoesNotExist


class BaseView(View):
    def get(self, request):
        levels = Levels.objects.all()
        topics = Topics.objects.all()
        topics1 = Topics.objects.filter(level__name='A1')
        topics2 = Topics.objects.filter(level__name='A2')
        topics3 = Topics.objects.filter(level__name='B1')
        topics4 = Topics.objects.filter(level__name='B2')
        context = {'levels': levels, 'topics': topics, 'topics1': topics1, 'topics2': topics2, 'topics3': topics3, 'topics4': topics4}
        return render(request, 'words/base.html', context)

# class BaseView(ListView):
#     template_name = 'words/base.html'
#     model = Topics
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         my_arg = self.kwargs.get('my_arg', None)
#         if my_arg:
#             queryset = queryset.filter(topic_id=my_arg)
#         return queryset


class UserToken(View):
    def get(self, request):
        try:
            token = Token.objects.get(user=self.request.user)
            context = {'token': token.key}
        except ObjectDoesNotExist:
            token = Token.objects.create(user=self.request.user)
            context = {'token': token.key}

        return render(request, 'words/token.html', context)


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

        context = {'word': random_word, 'one': one, 'two': two, 'three': three, 'four': four, 'test': my_arg}
        return render(request, 'words/test.html', context)


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

        my_arg = self.kwargs.get('my_arg', None)
        context = {'result': result, 'word': word, 'translation': translation, 'answer': my_arg}
        return render(request, 'words/check_translation.html', context)


class AddWord(LoginRequiredMixin, FormView):
    template_name = 'words/add_word.html'
    form_class = UserWordsForm
    success_url = reverse_lazy('show_words')
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


class ShowTests(LoginRequiredMixin, View):
    model = UserTests
    login_url = reverse_lazy('login')

    def get_queryset(self):
        queryset = UserTests.objects.filter(user=self.request.user)
        if queryset:
            user_test = queryset[0]
            return user_test
        else:
            return queryset

    # def get_user_test(self):
    #     user_tests = UserTests.objects.filter(user=self.request.user)
    #     if user_tests:
    #         user_test = user_tests[0]
    #         return user_test
    #     else:
    #         return user_tests

    def get_cleverest(self):
        all_tests = UserTests.objects.all()
        max_kpd = 0
        good_user = UserTests.objects.get(user=self.request.user)
        for test in all_tests:
            kpd = 100 / test.all_test * test.true_test
            if kpd >= max_kpd:
                max_kpd = kpd
                good_user = test
                good_user.max_kpd = int(max_kpd)
        return good_user

    def get_the_most_diligent(self):
        all_tests = UserTests.objects.all()
        max_tests = 0
        best_user = UserTests.objects.get(user=self.request.user)
        for test in all_tests:
            if test.all_test >= max_tests:
                max_tests = test.all_test
                best_user = test
        return best_user

    def get(self, request):
        user_result = self.get_queryset()
        max_kpd = self.get_cleverest()
        max_answers = self.get_the_most_diligent()
        context = {'user_result': user_result, 'max_kpd': max_kpd, 'max_answers': max_answers}
        print(context)
        return render(request, 'words/show_tests.html', context)


def translate(request):
    me = {'test': 'Тести з української', 'eng-test': 'Тести з англійської', 'choice': 'Вибиір варіанту',
          'eng-choice': 'Вибиір варіанту з англійської'}
    context = {'types': me}
    return render(request, 'words/translate.html', context)
