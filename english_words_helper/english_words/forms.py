from django import forms
from .models import UserWords


class UserWordsForm(forms.ModelForm):
    english_word = forms.CharField(label='Англійське слово')
    ukraine_word = forms.CharField(label='Українське слово')

    class Meta:
        model = UserWords
        fields = ['english_word', 'ukraine_word']
