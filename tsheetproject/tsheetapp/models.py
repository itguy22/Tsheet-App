from django.db import models

class TSheet(models.Model):
    headline = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=2000, default='Default description')