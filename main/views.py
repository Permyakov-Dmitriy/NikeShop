from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect

from auth_nike.models import NikeUser
from shop_nike.models import Product

from .models import FavoriteModel
from .forms import FavoriteForm


class Home(TemplateView):
    template_name = 'main/index.html'

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'main/profile.html'
    login_url = '/auth'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        favorites = FavoriteModel.objects.filter(user_id = self.request.user.id)
        context['fav'] = favorites

        context['user'] = self.request.user
        return context
    
class FavoriteView(View):
    def get(self, req, *args, **kwargs):
        return HttpResponseRedirect('/')
    
    def post(self, req, *args, **kwargs):
        form = FavoriteForm(req.POST)

        if form.is_valid():
            model = FavoriteModel()
            product_id = form.cleaned_data['product_id']

            model.user_id = NikeUser.objects.get(id=form.cleaned_data['user_id'])
            model.product_id = Product.objects.get(id=product_id)

            model.save()

        return HttpResponseRedirect(f'/shop/product/?id={product_id}')
