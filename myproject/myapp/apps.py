from django.apps import AppConfig


class MyappConfig(AppConfig):
    name = 'myapp'
    
    def ready(self): # this method conect the app with signals.py
        import myapp.signals