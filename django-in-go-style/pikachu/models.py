import uuid
from django.db import models

# Create your models here.

class Pikachu (models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.TextField(max_length=255)
    is_admin = models.BooleanField(default=False)
    age = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)