from django.apps import AppConfig


class TasklistingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'taskListing'

    def ready(self):
        print("starting scheduler")
        from . import schedular
        schedular.start()

