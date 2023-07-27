from typing import Any, Dict

from django.views.generic import TemplateView

from main.models import FavoriteModel



class BucketView(TemplateView):
    template_name = 'orders/bucket.html'

    def get_context_data(self, *args, **kwargs):
        return super().get_context_data(**kwargs)
        