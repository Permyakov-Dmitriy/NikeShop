from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404


from .models import Product


class ShopView(LoginRequiredMixin, TemplateView):
    template_name = 'shop_nike/shop.html'
    login_url = '/auth'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(gender=self.request.get_full_path().split('/')[-1])
        
        return context


class ProductView(LoginRequiredMixin, TemplateView):
    template_name = 'shop_nike/product.html'
    login_url = '/auth'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.GET.get('id', 1)

        try:
            context['prod'] = Product.objects.get(id = user_id)
        except ObjectDoesNotExist:
            raise Http404()

        context['user'] = self.request.user

        return context
