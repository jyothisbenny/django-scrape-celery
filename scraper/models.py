from django.db import models


# Create your models here.

class ScrapeData(models.Model):
    id = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=124, blank=True, null=True)
    protocol = models.CharField(max_length=124, blank=True, null=True)
    country = models.CharField(max_length=124, blank=True, null=True)
    uptime = models.CharField(max_length=124, blank=True, null=True)
    port = models.IntegerField()
