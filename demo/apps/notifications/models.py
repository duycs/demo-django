from django.db import models

from ..core.models import TimestampedModel

# Create your models here.


class NotificationsManager(models.Manager):

    def create_notice(self, type_notice, name, message):
        if not type_notice:
            raise ValueError("Notice must have type_notice")
        elif not name:
            raise ValueError("Notice must have name")
        elif not message:
            raise ValueError("Notice must have message")

        notice = self.model(type_notice=type_notice, name=name, message=message)
        notice.save()

        return notice


class Notifications(TimestampedModel):
    USER_NOTICES = "user_notices"
    SYSTEM_NOTICES = "system_notices"
    TYPE_NOTICE = [
        (USER_NOTICES, "User_notices"),
        (SYSTEM_NOTICES, "System_notices")
    ]

    type_notice = models.CharField(max_length=50, choices=TYPE_NOTICE)
    name = models.CharField(max_length=100)
    message = models.TextField()
    
    objects = NotificationsManager()

    def __str__(self):
        return self.type_notice
