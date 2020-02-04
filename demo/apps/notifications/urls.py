from django.urls import path

from .views import NotificationsAPIView

app_name = 'notifications'

"""
urls for CRUD notifications with methods implemented in NotificationsAPIView
"""
urlpatterns = [
    path("notifications", NotificationsAPIView.as_view()),
    path("notifications/<int:id>", NotificationsAPIView.as_view()),
]
