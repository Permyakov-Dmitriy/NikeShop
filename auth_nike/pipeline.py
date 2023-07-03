from social_core.backends.vk import VKOAuth2
from social_core.pipeline.partial import partial
from django.shortcuts import redirect


@partial
def send_email(backend, user, *args, **kwargs):
    if isinstance(backend, VKOAuth2):
        return redirect('VKEmail')


@partial
def save_email(backend, user, request, details, is_new=False, *args, **kwargs):
    if is_new and isinstance(backend, VKOAuth2):
        email = request.session.get('email')
        print(kwargs)
        if email:
            user.email = email
            user.save()