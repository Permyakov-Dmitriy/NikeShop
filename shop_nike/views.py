from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404


from .models import Product
from main.models import FavoriteModel
from auth_nike.models import NikeUser


class ShopView(LoginRequiredMixin, TemplateView):
    template_name = 'shop_nike/shop.html'
    login_url = '/auth'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        gender = self.request.GET.get('gender', '')
        category = self.request.GET.get('category', '')

        products = Product.objects.filter(gender=gender)

        if category:
            products = products.filter(category=category)

        context['gender'] = gender
        context['products'] = products.order_by('?')
        
        return context


class ProductView(LoginRequiredMixin, TemplateView):
    template_name = 'shop_nike/product.html'
    login_url = '/auth'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = self.request.GET.get('id', 1)
        user = NikeUser.objects.get(id=self.request.user.id)

        try:
            product = Product.objects.get(id = product_id)
        except ObjectDoesNotExist:
            raise Http404()
        
        try:
            favorite = FavoriteModel.objects.get(product_id=product, user_id=user)
            fav_id = favorite.id
            isFav = True
        except ObjectDoesNotExist:
            fav_id = None
            isFav = False

        context['isFav'] = isFav
        context['fav_id'] = fav_id
        context['user'] = self.request.user
        context['prod'] = product

        return context


class ProductsSearchView(LoginRequiredMixin, TemplateView):
    template_name = 'shop_nike/shop.html'
    login_url = '/auth'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search = '.*' + self.request.GET.get('search', '') + '.*'

        products = Product.objects.filter(title_product__iregex=search)

        context['products'] = products
        
        return context