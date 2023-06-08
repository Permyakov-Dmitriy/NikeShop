from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class Home(TemplateView):
    template_name = 'main/index.html'

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'main/profile.html'
    login_url = '/auth'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
