from english_words import models
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class SerTopics(serializers.ModelSerializer):
    level = serializers.StringRelatedField()

    class Meta:
        model = models.Topics
        fields = '__all__'


class SerLevels(serializers.ModelSerializer):
    class Meta:
        model = models.Levels
        fields = '__all__'


class SerWords(serializers.ModelSerializer):
    topic = serializers.SlugRelatedField(slug_field='name', read_only=True)
    topic_id = serializers.PrimaryKeyRelatedField(queryset=models.Topics.objects.all(), write_only=True, source='topic')
    level = serializers.StringRelatedField(source='topic.level.name')

    class Meta:
        model = models.Words
        fields = ['id', 'level', 'topic', 'in_english', 'in_ukrainian', 'topic_id']


class SerIrregularVerbs(serializers.ModelSerializer):
    class Meta:
        model = models.IrregularVerbs
        fields = '__all__'


class SerUserWords(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.UserWords
        fields = '__all__'
        read_only_fields = ('user',)


class SerUserToken(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['key']


class SerResults(serializers.ModelSerializer):
    class Meta:
        model = models.UserTests
        fields = ['all_test', 'true_test', 'false_test']
