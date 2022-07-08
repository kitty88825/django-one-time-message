import uuid

from django.db import models


class Card(models.Model):
    recipient = models.CharField(max_length=50, null=True)
    content = models.TextField()
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    count = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return str(self.token)
