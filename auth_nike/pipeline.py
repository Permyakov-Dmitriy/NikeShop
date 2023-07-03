# from social_core.backends.vk import VKOAuth2
# from django.http import HttpResponseForbidden


# class CustomVKAuthPipeline:
#     def __init__(self, *args, **kwargs) -> None:
#         pass

#     def __call__(self, request):
#         response = self.process_request(request)
#         if response is None:
#             response = self.get_response(request)
#         return response

#     def auth_allowed(self, strategy, details, backend, user=None, *args, **kwargs):
#         if isinstance(backend, VKOAuth2):
#             # Выполняйте свои дополнительные действия
#             # перед разрешением аутентификации через VK.

#             # Выводим полученные данные для демонстрации
#             print(details)

#         # Возвращаем None, чтобы передать управление следующему методу в пайплайне
#         return None

#     def pre_social_auth(self, strategy, details, backend, user=None, *args, **kwargs):
#         if isinstance(backend, VKOAuth2):
#             # Выполняйте свои дополнительные действия
#             # перед началом социальной аутентификации через VK.

#             # Выводим полученные данные для демонстрации
#             print(details)

#         # Возвращаем None, чтобы передать управление следующему методу в пайплайне
#         return None

#     def social_auth(self, strategy, details, backend, user=None, *args, **kwargs):
#         if isinstance(backend, VKOAuth2):
#             # Выполняйте свои дополнительные действия
#             # во время социальной аутентификации через VK.

#             # Выводим полученные данные для демонстрации
#             print(details)

#         # Возвращаем None, чтобы передать управление следующему методу в пайплайне
#         return None

#     def post_social_auth(self, strategy, details, backend, user=None, *args, **kwargs):
#         if isinstance(backend, VKOAuth2):
#             # Выполняйте свои дополнительные действия
#             # после успешной социальной аутентификации через VK.

#             # Выводим полученные данные для демонстрации
#             print(details)

#         # Возвращаем None, чтобы передать управление следующему методу в пайплайне
#         return None

#     def get_user_details(self, strategy, details, backend, user=None, *args, **kwargs):
#         if isinstance(backend, VKOAuth2):
#             # Выполняйте свои дополнительные действия
#             # при получении данных пользователя из VK.

#             # Выводим полученные данные для демонстрации
#             print(details)

#         # Возвращаем None, чтобы передать управление следующему методу в пайплайне
#         return None


def create_profile(backend, user, *args, **kwargs):
    print(backend)
    print(user)
    print(args)
    kwargs['details']['email'] = kwargs['details']['first_name'] + '@gmail.com'