from django.apps import AppConfig


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
    #git add . ,git commit -m "Your descriptive commit message" ,git push origin branch-name