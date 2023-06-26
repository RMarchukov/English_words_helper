from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.views import View
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import RegisterUserForm, LoginForm
from django.contrib.auth.views import LoginView


class RegisterView(FormView):
    template_name = 'users/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super(RegisterView, self).form_valid(form)
        # if password1 != password2:
        #     return AttributeError
        # else:
        #     user = authenticate(username=username, password=password1, email=email)
        #     login(self.request, user)
        #     return super(RegisterView, self).form_valid(form)


class LoginView(FormView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('base')
    form_class = LoginForm

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return super(LoginView, self).form_valid(form)
        return self.form_invalid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
