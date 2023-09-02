from django.apps import AppConfig


class PollsConfig(AppConfig):
    """
    A class responsible for polls app configuration. there are 2 attributes
    in this class, name and default_auto_field.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
