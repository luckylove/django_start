from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # importing the signals for the profile here
    def ready(self):
        import users.signals
