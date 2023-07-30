from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect

from auth_nike.models import NikeUser
from shop_nike.models import Product

from .models import FavoriteModel
from .forms import FavoriteForm, FavoriteDeleteForm


# Главная страница
class Home(TemplateView):
    template_name = 'main/index.html'

# Профиль с проверкой на авторизацию пользователя
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'main/profile.html'
    login_url = '/auth'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Все избранные продукты пользователя
        favorites = FavoriteModel.objects.filter(user_id = self.request.user.id)

        context['fav'] = favorites
        context['user'] = self.request.user

        return context

# Добавление в избранное
class FavoriteView(View):
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

