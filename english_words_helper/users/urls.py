from django.urls import path
from .views import RegisterView, LogoutView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login_main'),
    path('logout/', LogoutView.as_view(), name='logout_main'),
]
