from social_core.pipeline.partial import partial
from django.shortcuts import redirect, render


@partial
def send_email(backend, user, request, details, is_new=False, *args, **kwargs):
    e = request.session.get('email', '')
    print(user)
    print(details)
    print(e)
    
    if is_new and not details['email']:
        if not e:
            return redirect('VKEmail')
        
        else:
            # TODO fix
            details['email'] = e
            # user.email = e

            # try:
            #     user.save()
            # except Exception:
            #     return render(request, 'auth_nike/VKEmail.html', {'err': 'Почта уже существует'})
