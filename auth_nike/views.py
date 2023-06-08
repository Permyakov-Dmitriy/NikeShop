from django.template.response import TemplateResponse
from django.views.generic import View
from .forms import UserNikeReg, UserNikeAuth
from django.http.response import HttpResponseRedirect
from .models import NikeUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, logout
from django.db import IntegrityError


class RegView(View):
    def get(self, req, *args, **kwargs):
        return TemplateResponse(req, 'auth_nike/register.html', {'err': ''})

    def post(self, req, *args, **kwargs):
        form = UserNikeReg(req.POST)

        if form.is_valid():
            model = NikeUser()
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
                return TemplateResponse(req, 'auth_nike/register.html', {'err': 'Пользователь с такой почтой уже существует'})

            user = NikeUser.objects.get(email=email)
            if user.check_password(password):
                login(req, user)

        else:
            return TemplateResponse(req, 'auth_nike/register.html', {'err': 'Заполните все поля'})
                            
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
        print(1)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = NikeUser.objects.get(email=email)
            if user.check_password(password):
                    login(req, user)
        else:
            return TemplateResponse(req, 'auth_nike/login.html', {'err': 'Заполните все поля'})

        return HttpResponseRedirect('/profile')