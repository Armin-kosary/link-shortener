from django.db import models

# Create your models here.

class Link(models.Model):
    main_link = models.TextField()
    short_link = models.CharField(max_length=10)