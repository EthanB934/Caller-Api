from django.db import models

class Calls(models.Model):
    number = models.CharField(max_length=10)