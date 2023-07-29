from django.views.generic import TemplateView, View

from django.db.models import Count

from django.http.response import HttpResponseRedirect

from main.models import FavoriteModel
from shop_nike.models import Product
from .models import BucketModel

from .forms import BucketForm

from auth_nike.models import NikeUser
from shop_nike.models import Product


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
    

class BucketAddView(View):
    def post(self, req, *args, **kwargs):
        form = BucketForm(req.POST)

        if form.is_valid():
            product_id = form.cleaned_data['product_id']
            bucket = BucketModel.objects.filter(product_id = product_id)

            if len(bucket) == 9:
                return HttpResponseRedirect(f'/shop/product/?id={product_id}')

            model = BucketModel()

            model.user_id = NikeUser.objects.get(id=form.cleaned_data['user_id'])
            model.product_id = Product.objects.get(id=product_id)

            model.save()

        return HttpResponseRedirect(f'/shop/product/?id={product_id}')