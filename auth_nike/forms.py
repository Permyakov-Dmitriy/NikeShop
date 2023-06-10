from django.forms import Form, CharField, EmailField, DateField
from django.contrib.auth.forms import SetPasswordForm, PasswordResetForm


class UserNikeReg(Form):
    first_name = CharField(max_length=20)
    last_name = CharField(max_length=30)
    email = EmailField()
    password = CharField(max_length=50)
    birth_day = DateField()

class UserNikeAuth(Form):
    email = EmailField()
    password = CharField(max_length=50)


class UserSetNewPasswordForm(SetPasswordForm):
    new_password1 = CharField(max_length=50)
    new_password2 = CharField(max_length=50)


class UserForgotPasswordForm(PasswordResetForm):
    email = EmailField()


class ChangeEmailFrom(Form):
    new_email = EmailField()
    old_email = EmailField()
    password = CharField(max_length=50)