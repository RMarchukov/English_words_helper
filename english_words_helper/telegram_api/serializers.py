from english_words import models
from rest_framework import serializers


class SerTopics(serializers.ModelSerializer):
    level = serializers.StringRelatedField()
    topic = serializers.CharField(max_length=64, source='name')

    class Meta:
        model = models.Topics
        fields = ['topic', 'level']


class SerLevels(serializers.ModelSerializer):
    class Meta:
        model = models.Levels
        fields = ['name', ]


class SerWords(serializers.ModelSerializer):
    topic = serializers.StringRelatedField(source='topic.name')
    level = serializers.StringRelatedField(source='topic.level')

    class Meta:
        model = models.Words
        exclude = ['id', ]


class SerIrregularVerbs(serializers.ModelSerializer):
    class Meta:
        model = models.IrregularVerbs
        exclude = ['id', ]
