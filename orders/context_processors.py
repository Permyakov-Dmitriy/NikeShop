from .models import Basket
from auth_nike.models import NikeUser

def CheckBasket(request):
    user = NikeUser.objects.get(email=request.user)

    return {'full_basket': bool(Basket.objects.filter(user_id=user.id))}