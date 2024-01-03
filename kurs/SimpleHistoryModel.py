from django.db import models
from simple_history.models import SimpleHistoryModel

class CustomerModel(SimpleHistoryModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
