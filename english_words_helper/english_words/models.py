from django.db import models
from django.contrib.auth.models import User


class Levels(models.Model):
    name = models.CharField(max_length=10, null=True, unique=True, default='A1')

    def __str__(self):
        return f'{self.name}'


class Topics(models.Model):
    name = models.CharField(max_length=64, null=True, unique=False)
    level = models.ForeignKey(Levels, on_delete=models.CASCADE, null=True, related_name='topic')

    def __str__(self):
        return f'{self.name}, {self.level}'


class Words(models.Model):
    in_english = models.CharField(max_length=64)
    in_ukrainian = models.CharField(max_length=64)
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE, related_name='word', null=True)

    def __str__(self):
        return f'{self.in_english}, {self.in_ukrainian}, {self.topic}'


class IrregularVerbs(models.Model):
    first_form = models.CharField(max_length=64)
    second_form = models.CharField(max_length=64)
    third_form = models.CharField(max_length=64)
    translate = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.first_form}, {self.second_form}, {self.third_form}, {self.translate}'


class UserWords(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    english_word = models.CharField(max_length=64)
    ukraine_word = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.english_word}, {self.ukraine_word}'


class UserTests(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    all_test = models.IntegerField(default=0)
    true_test = models.IntegerField(default=0)
    false_test = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user}'
