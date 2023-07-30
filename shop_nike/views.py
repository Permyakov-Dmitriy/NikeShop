from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.db.models import Count

from .models import Product
from main.models import FavoriteModel
from auth_nike.models import NikeUser
from orders.models import Basket


class ShopView(LoginRequiredMixin, TemplateView):
    ''' Страница магазина с продуктами '''
    template_name = 'shop_nike/shop.html'
    login_url = '/auth'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Гендер продуктов
        gender = self.request.GET.get('gender', '')
        # Категория продуктов
        category = self.request.GET.get('category', '')

        # Фильтрация по гендеру для последующего фильтра по категории
        products = Product.objects.filter(gender=gender)

        if category:
            products = products.filter(category=category)

        context['gender'] = gender
        # Случайная сортировка продуктов
        context['products'] = products.order_by('?')
        
        return context


class ProductView(LoginRequiredMixin, TemplateView):
    ''' Страница продукта '''
    template_name = 'shop_nike/product.html'
    login_url = '/auth'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Вытаскиваем id продукта если нет то савим 0 для будущего провоцирования ошибки
        product_id = self.request.GET.get('id', 0)

        user = NikeUser.objects.get(id=self.request.user.id)

        # Если продукта с таким id нет то возвращаем страницу 404
        try:
            product = Product.objects.get(id = product_id)
        except ObjectDoesNotExist:
            raise Http404()
        
        # Берем продукт из карзины для установки лимита на добавления
        bucket = Basket.objects.filter(product_id = product_id)
        limit = len(bucket) == 9
        
        # Рекомендации основанные на самых за лайканых продукциях
        
        # Фильтруем продукты имеющие лайки по гендеру
        fav_fltr_gender = FavoriteModel.objects.filter(product_id__gender=product.gender)

        # Группируем по product_id и агрегируем по количеству лайков затем сортируем от большего к меньшему
        recomend_prod_on_fav = fav_fltr_gender.values('product_id') \
        .annotate(total_products=Count('user_id')).order_by('-total_products')

        # Массив для последующего формирования списка самых залайканчх продуктов
        product_ids = [item['product_id'] for item in recomend_prod_on_fav]

        # Выбираем только те продукты которые есть в массиве и только первые три 
        recomend_list_products = Product.objects.filter(id__in=product_ids)[:3]

        # Установка id избранного и проверки на избранное
        try:
            favorite = FavoriteModel.objects.get(product_id=product, user_id=user)
            fav_id = favorite.id
            isFav = True
        except ObjectDoesNotExist:
            fav_id = None
            isFav = False

        # Контекстные значения для шаблона
        context['limit'] = limit
        context['list_recomend'] = recomend_list_products
        context['isFav'] = isFav
        context['fav_id'] = fav_id
        context['user'] = self.request.user
        context['prod'] = product

        return context


class ProductsSearchView(LoginRequiredMixin, TemplateView):
    ''' Поиск продукта '''
    template_name = 'shop_nike/shop.html'
    login_url = '/auth'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Формирование строки для LIKE запроса в SQL
        search = '.*' + self.request.GET.get('search', '') + '.*'

        products = Product.objects.filter(title_product__iregex=search)

        context['products'] = products
        
        return context