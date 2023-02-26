from django.db import models


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
