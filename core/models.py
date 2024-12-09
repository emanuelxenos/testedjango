from django.db import models

# Create your models here.
class People(models.Model):
    fullname = models.CharField(max_length=80)
    years = models.CharField(max_length=3)
    email = models.CharField(max_length=80)
    def __str__(self):
        return self.fullname
    