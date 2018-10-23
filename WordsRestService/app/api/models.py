from django.db import models

class Words(models.Model):
    id = models.AutoField(primary_key=True)
    color = models.CharField(max_length=10, blank=True)
    words = models.TextField(blank=False)
    countwords = models.IntegerField(blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)