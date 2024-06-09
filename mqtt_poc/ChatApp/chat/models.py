from django.db import models

from common.models import BaseModel


# Create your models here.
class Message(BaseModel):
    room = models.CharField(max_length=20)
    content = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"[{self.room}] {self.content}"
