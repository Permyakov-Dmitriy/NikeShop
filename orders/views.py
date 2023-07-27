from typing import Any, Dict

from django.views.generic import TemplateView

from main.models import FavoriteModel
from shop_nike.models import Product

from django.db.models import Count


class BucketView(TemplateView):
    template_name = 'orders/bucket.html'

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

        context['list_recomend'] = recomend_list_products

        return context