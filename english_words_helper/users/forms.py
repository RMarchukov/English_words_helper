from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введіть логін', 'class': 'form-input'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Введіть email', 'class': 'form-input'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введіть пароль', 'class': 'form-input'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введіть пароль знову', 'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логін', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ['username', 'password']
