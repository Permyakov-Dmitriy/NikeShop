from django.views.generic import TemplateView, View

from django.db.models import Count

from django.http.response import HttpResponseRedirect

from django.contrib.auth.mixins import LoginRequiredMixin

from main.models import FavoriteModel
from shop_nike.models import Product
from auth_nike.models import NikeUser
from .models import Basket

from .forms import BasketForm


class BasketView(LoginRequiredMixin, TemplateView):
    ''' Корзина покупок '''
    template_name = 'orders/bucket.html'
    login_url = '/auth'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        # Все лайки
        all_fav = FavoriteModel.objects.all()

        # Группируем по product_id и агрегируем по количеству лайков затем сортируем от большего к меньшему
        recomend_prod_on_fav = all_fav.values('product_id') \
        .annotate(total_products=Count('user_id')).order_by('-total_products')

        # Массив для последующего формирования списка самых залайканчх продуктов
        product_ids = [item['product_id'] for item in recomend_prod_on_fav]

        # Выбираем только те продукты которые есть в массиве и только первые три 
        recomend_list_products = Product.objects.filter(id__in=product_ids)[:3]

        all_products_on_basket = Basket.objects.filter(user_id=self.request.user.id) 

        context['list_recomend'] = recomend_list_products
        context['products'] = all_products_on_basket

        return context
    

class BascketAddView(LoginRequiredMixin, View):
    ''' Удаление из корзины покупок  '''
    login_url = '/auth'

    def post(self, req, *args, **kwargs):
        form = BasketForm(req.POST)

        if form.is_valid():
            product_id = form.cleaned_data['product_id']
            user_id = form.cleaned_data['user_id']

            user = NikeUser.objects.get(id=user_id)
            product = Product.objects.get(id=product_id)

            product_in_basket, created = Basket.objects.get_or_create(
                user_id=user,
                product_id=product,
                )

            if not created:
                # Если кол-во 9 то редирект обратно на страницу продукта с блокировкой на добавление
                if product_in_basket.quantity == 9:
                    return HttpResponseRedirect(f'/shop/product/?id={product_id}')

                product_in_basket.quantity += 1
                product_in_basket.save()


        return HttpResponseRedirect(f'/shop/product/?id={product_id}')