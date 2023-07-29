from django.forms import Form, IntegerField


class BucketForm(Form):
    user_id = IntegerField()
    product_id = IntegerField()