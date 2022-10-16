from django.db import models

class B_categories(models.Model):
    name = models.CharField(max_length=20)