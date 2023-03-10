from django import forms
from .models import UserWords


class UserWordsForm(forms.ModelForm):
    class Meta:
        model = UserWords
        fields = ['english_word', 'ukraine_word']
