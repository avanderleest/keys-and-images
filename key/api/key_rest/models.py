from django.db import models

# Create your models here.
class APIIntegrationKey(models.Model):
    token = models.CharField(max_length=50, unique = True),
    count = models.PositiveBigIntegerField()
