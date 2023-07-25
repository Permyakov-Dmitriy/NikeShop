from django.views.generic import TemplateView


class BucketView(TemplateView):
    template_name = 'orders/bucket.html'
