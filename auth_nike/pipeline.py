from social_core.backends.vk import VKOAuth2
from social_core.pipeline.partial import partial
from django.shortcuts import redirect, render


@partial
def send_email(backend, user, request, details, is_new=False, *args, **kwargs):
    e = request.session.get('email', '')
    print(e)

    # TODO поменять конструкцию
    
    if not e and not details['email']:
        print(0)
        return redirect('VKEmail')
    
    elif not details['email']:
        details['email'] = e
        user.email = e

        try:
            user.save()
        except Exception:
            return render(request, 'auth_nike/VKEmail.html', {'err': 'Почта уже существует'})


@partial
def save_email(backend, user, request, details, is_new=False, *args, **kwargs):
    # if is_new and isinstance(backend, VKOAuth2):
    #     email = request.session.get('email')
    #     print(kwargs)
    #     if email:
    #         user.email = email
    #         user.save()
    ...
