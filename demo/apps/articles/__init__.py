from django.apps import AppConfig


class ArticlesAppConfig(AppConfig):
    name = 'demo.apps.articles'
    label = 'articles'
    verbose_name = 'Articles'

    def ready(self):
        import demo.apps.articles.signals

default_app_config = 'demo.apps.articles.ArticlesAppConfig'