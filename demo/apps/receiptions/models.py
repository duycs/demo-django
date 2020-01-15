from django.db import models

# Create your models here.
from datetime import datetime

class Receiption(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    # def __init__(self, email, content, created=None):
    #     self.email = email
    #     self.content = content
    #     self.created = created or datetime.now()

#receiptions = Receiption(email='leila@example.com', content='foo bar')