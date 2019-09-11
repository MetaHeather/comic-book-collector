from django.db import models

# Create your models here.
class Comic(models.Model):
    title = models.CharField(max_length=100)
    issue = models.IntegerField()
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    publishdate = models.DateField()