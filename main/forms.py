from django.forms import Form, IntegerField


class FavoriteForm(Form):
    user_id = IntegerField()
    product_id = IntegerField()