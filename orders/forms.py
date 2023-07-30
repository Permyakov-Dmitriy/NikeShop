from django.forms import Form, IntegerField


class BasketForm(Form):
    user_id = IntegerField()
    product_id = IntegerField()