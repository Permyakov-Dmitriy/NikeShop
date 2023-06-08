from django.forms import Form, CharField, EmailField, DateField

class UserNikeReg(Form):
    first_name = CharField(max_length=20)
    last_name = CharField(max_length=30)
    email = EmailField()
    password = CharField(max_length=50)
    birth_day = DateField()

class UserNikeAuth(Form):
    email = EmailField()
    password = CharField(max_length=50)
