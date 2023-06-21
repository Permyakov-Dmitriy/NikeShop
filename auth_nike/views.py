from django.template.response import TemplateResponse
from django.views.generic import View
from django.http.response import HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, logout
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.db import IntegrityError
from django.urls import reverse_lazy

from .models import NikeUser
from .forms import UserNikeReg, UserNikeAuth, UserSetNewPasswordForm, UserForgotPasswordForm, ChangeEmailFrom


class RegView(UserPassesTestMixin, View):
    def test_func(self):
        return not self.request.user.is_authenticated
    
    def handle_no_permission(self):
        return HttpResponseRedirect('/')

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
    
class AuthView(UserPassesTestMixin, View):
    def test_func(self):
        return not self.request.user.is_authenticated
    
    def handle_no_permission(self):
        return HttpResponseRedirect('/')

    def get(self, req, *args, **kwargs):
        return TemplateResponse(req, 'auth_nike/login.html')
    
    def post(self, req, *args, **kwargs):
        form = UserNikeAuth(req.POST)
        err = False

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = NikeUser.objects.get(email=email)

                if user.check_password(password):
                    login(req, user)
                else:
                    err = 'Неверный пароль'
                    
            except NikeUser.DoesNotExist:
                err = 'Пользователя с такой почтой не существует'
            
        else:
            err = 'Заполните все поля'

        if err:
            return TemplateResponse(req, 'auth_nike/login.html', {'err': err})
        
        return HttpResponseRedirect('/profile')
    

class UserForgotPasswordView(PasswordResetView):
    """
    Представление по сбросу пароля по почте
    """
    form_class = UserForgotPasswordForm
    template_name = 'auth_nike/user_password_reset.html'
    success_url = reverse_lazy('home')

    subject_template_name = 'auth_nike/email/password_subject_reset_mail.txt'
    email_template_name = 'auth_nike/email/password_reset_mail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Запрос на восстановление пароля'
        
        return context


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    """
    Представление установки нового пароля
    """
    form_class = UserSetNewPasswordForm
    template_name = 'auth_nike/user_password_set_new.html'
    success_url = reverse_lazy('home')


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