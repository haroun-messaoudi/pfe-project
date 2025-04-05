from django.apps import AppConfig


class EstablishementsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'establishements'
    def ready(self):
        import establishements.index

    
