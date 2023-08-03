from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect

from auth_nike.models import NikeUser
from shop_nike.models import Product

from .models import FavoriteModel
from .forms import FavoriteForm, FavoriteDeleteForm


class Home(TemplateView):
    ''' Главная страница '''
    template_name = 'main/index.html'

class ProfileView(LoginRequiredMixin, TemplateView):
    ''' Профиль с проверкой на авторизацию пользователя '''
    template_name = 'main/profile.html'
    login_url = '/auth'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Все избранные продукты пользователя
        favorites = FavoriteModel.objects.filter(user_id = self.request.user.id)

        context['fav'] = favorites
        context['user'] = self.request.user

        return context

class FavoriteView(View):
    ''' Добавление в избранное '''
    def post(self, req, *args, **kwargs):
        form = FavoriteForm(req.POST)

        if form.is_valid():
            model = FavoriteModel()
            product_id = form.cleaned_data['product_id']

            model.user_id = NikeUser.objects.get(id=form.cleaned_data['user_id'])
            model.product_id = Product.objects.get(id=product_id)

            model.save()

        return HttpResponseRedirect(f'/shop/product/?id={product_id}')
    

class FavoriteDeleteView(View):
    ''' Удаление из избранных '''
    def post(self, req, *args, **kwargs):
        form = FavoriteDeleteForm(req.POST)

        if form.is_valid():
            product_id = form.cleaned_data['product_id']
            fav_id = form.cleaned_data['fav_id']

            # Достаем обьект пользователя для удаления из избранного
            user = NikeUser.objects.get(id=self.request.user.id)

            fav = FavoriteModel.objects.get(id=fav_id, user_id=user)

            fav.delete()

        return HttpResponseRedirect(f'/shop/product/?id={product_id}')

