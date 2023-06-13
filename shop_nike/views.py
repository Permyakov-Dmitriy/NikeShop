from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Product


class ShopView(LoginRequiredMixin, TemplateView):
    template_name = 'shop_nike/shop.html'
    login_url = '/auth'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.request.get_full_path().split('/')[-1])
        context['products'] = Product.objects.filter(gender=self.request.get_full_path().split('/')[-1])
        return context
