from .models import Basket
from auth_nike.models import NikeUser

class CheckBasketMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def process_response(self, request, response):
        response.context_data['custom_data'] = bool(Basket.objects.filter(user_id=NikeUser.objects.get(id=response.context_data['user_id'])))
        print(response.context_data)
        return response

    def __call__(self, request):
        response = self.get_response(request)
        response = self.process_response(request, response)
        return response
