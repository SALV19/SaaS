from django.db import models

# Create your models here.
class PageVisits(models.Model):
  # db -> table
  # id -> primary key: auto_fill
  path = models.TextField(null=True, blank=True)
  time_stamps = models.DateTimeField(auto_now_add=True)