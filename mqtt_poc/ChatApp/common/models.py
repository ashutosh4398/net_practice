from uuid import uuid4

from django.db import models


# Create your models here.
class BaseModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    id = models.UUIDField(primary_key=True, default=uuid4)

    class Meta:
        abstract = True
