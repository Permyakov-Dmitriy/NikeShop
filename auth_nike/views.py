from django.template.response import TemplateResponse
from django.views.generic import View
from django.http.response import HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, logout
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.contrib.messages.views import SuccessMessageMixin
from django.db import IntegrityError
from django.urls import reverse_lazy

from .models import NikeUser
from .forms import UserNikeReg, UserNikeAuth, UserSetNewPasswordForm, UserForgotPasswordForm, ChangeEmailFrom


class RegView(View):
    def get(self, req, *args, **kwargs):
        return TemplateResponse(req, 'auth_nike/register.html', {'err': ''})

    def post(self, req, *args, **kwargs):
        form = UserNikeReg(req.POST)

        if form.is_valid():
            model = NikeUser()
            err = False

            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            
            model.first_name = form.cleaned_data['first_name']
            model.last_name = form.cleaned_data['last_name']
            model.email = email
            model.password = make_password(password)
            model.birth_day = form.cleaned_data['birth_day']

            try:
                model.save()
            except IntegrityError:
                err = 'Пользователь с такой почтой уже существует'

            user = NikeUser.objects.get(email=email)
            if user.check_password(password):
                login(req, user)

        else:
            err = 'Заполните все поля'

        if err:
            return TemplateResponse(req, 'auth_nike/register.html', {'err': err})
        
        return HttpResponseRedirect('/profile')
    
class LogoutView(View):
    def post(self, req, *args, **kwargs):
        logout(req)

        return HttpResponseRedirect('/')
    
class AuthView(View):
    def get(self, req, *args, **kwargs):
        return TemplateResponse(req, 'auth_nike/login.html')
    
    def post(self, req, *args, **kwargs):
        form = UserNikeAuth(req.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = NikeUser.objects.get(email=email)
            except NikeUser.DoesNotExist:
                return TemplateResponse(req, 'auth_nike/login.html', {'err': 'Пользователя с такой почтой не существует'})
            
            if user.check_password(password):
                    login(req, user)
            else:
                return TemplateResponse(req, 'auth_nike/login.html', {'err': 'Неверный пароль'})
        else:
            return TemplateResponse(req, 'auth_nike/login.html', {'err': 'Заполните все поля'})

        return HttpResponseRedirect('/profile')
    

class UserForgotPasswordView(SuccessMessageMixin, PasswordResetView):
    """
    Представление по сбросу пароля по почте
    """
    form_class = UserForgotPasswordForm
    template_name = 'auth_nike/user_password_reset.html'
    success_url = reverse_lazy('home')
    success_message = 'Письмо с инструкцией по восстановлению пароля отправлена на ваш email'

    subject_template_name = 'auth_nike/email/password_subject_reset_mail.txt'
    email_template_name = 'auth_nike/email/password_reset_mail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Запрос на восстановление пароля'
        
        return context


class UserPasswordResetConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
    """
    Представление установки нового пароля
    """
    form_class = UserSetNewPasswordForm
    template_name = 'auth_nike/user_password_set_new.html'
    success_url = reverse_lazy('home')
    success_message = 'Пароль успешно изменен. Можете авторизоваться на сайте.'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Установить новый пароль'

        return context
    

class ChangeEmail(View):
    def get(self, req, *args, **kwargs):
        return TemplateResponse(req, 'auth_nike/change_password.html')
    
    def post(self, req, *args, **kwargs):
        form = ChangeEmailFrom(req.POST)
        err = False

        if form.is_valid():
            password = form.cleaned_data['password']
            old_email = form.cleaned_data['old_email']
            new_email = form.cleaned_data['new_email']

            user = NikeUser.objects.get(email = old_email)

            if user.check_password(password):
                user.email = new_email
                try:
                    user.save()
                except IntegrityError:
                    err = 'Аккаунт с такой почтой уже существует'
            else:
                err = 'Неверный пароль'
        else:
            err = 'Заполните все поля'

        if err:
            return TemplateResponse(req, 'auth_nike/change_password.html', {'error': err})
        
        return HttpResponseRedirect('/profile/')