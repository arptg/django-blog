from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'Users'

    # Overridden method to use signals from the file
    def ready(self):
        import Users.signals
