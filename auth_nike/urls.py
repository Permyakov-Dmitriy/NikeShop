from django.urls import path

from main.views import ProfileView
from .views import LogoutView, ChangeEmail, UserForgotPasswordView, UserPasswordResetConfirmView, VKEmailView


url_reset_password = [
    path('', UserForgotPasswordView.as_view(), name='password_reset'),
    path('set-new-password/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]

url_profile = [
    path('', ProfileView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('change-email/', ChangeEmail.as_view())
]