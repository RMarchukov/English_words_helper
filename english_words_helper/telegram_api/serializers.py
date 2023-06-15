from english_words import models
from rest_framework import serializers


class SerTopic(serializers.ModelSerializer):
    class Meta:
        model = models.Topics
        fields = ['name', 'level_id']
