from django.urls import re_path, include, path
from django.conf import settings
from django.contrib.staticfiles import views as static_views

from . import views

app_name = "com"

urlpatterns = [

    path('login/', views.login_view, name='login'),
    # path("",views.MasterView.as_view()),
]
