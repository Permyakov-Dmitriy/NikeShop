from NikeShop.celery import app
from celery import shared_task

from datetime import timedelta, datetime
from auth_nike.models import NikeUser
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from NikeShop.settings import DEFAULT_FROM_EMAIL


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    # sender.add_periodic_task(timedelta(minutes=1), check_birth_day_task.s(), name='check_birth_day_task')

@shared_task
def test():
    print('Hello')

# @app.task
# def check_birth_day_task():
#     print(123)
#     now = datetime.now().strftime("%Y-%m-%d")
#     your_model_objects = NikeUser.objects.filter(birth_day = now)

#     recipient_list = []
#     html_content  = render_to_string('main/birth_day_congrat.html', {})
#     from_email = DEFAULT_FROM_EMAIL
#     subject = 'С днем пождения!'
#     message = ''

#     for obj in your_model_objects:
#         recipient_list.append(obj.email)

#     email = EmailMessage(subject, message, from_email, recipient_list)
#     email.content_subtype = 'html'  # Устанавливаем тип контента как HTML
#     email.attach_alternative(html_content, "text/html")  # Прикрепляем HTML-версию сообщения

#     email.send()
