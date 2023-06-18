from celery import shared_task

from datetime import timedelta, datetime
from auth_nike.models import NikeUser
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from NikeShop.settings import DEFAULT_FROM_EMAIL


# @app.on_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     print("Настройка задач выполнена")
#     sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    # sender.add_periodic_task(timedelta(minutes=1), check_birth_day_task.s(), name='check_birth_day_task')


@shared_task
def check_birth_day_task():
    now = datetime.now().strftime("%Y-%m-%d")
    your_model_objects = NikeUser.objects.filter(birth_day = now)

    from_email = DEFAULT_FROM_EMAIL
    subject = 'С ДНЁМ РОЖДЕНИЯ!'
    message = ''

    for obj in your_model_objects:
        html_content  = render_to_string('main/birth_day_congrat.html', {'name': obj.first_name, 'last_name': obj.last_name})

        email = EmailMultiAlternatives(subject, message, from_email, [obj.email])
        email.attach_alternative(html_content, "text/html") 

        email.send()
