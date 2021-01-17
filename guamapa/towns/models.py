from django.db import models
import uuid


class Town(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    name = models.CharField(max_length=200)