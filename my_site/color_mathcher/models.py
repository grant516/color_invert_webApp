from django.db import models

# Create your models here.
class Colors(models.Model):

    red = models.CharField(max_length=100)
    green = models.CharField(max_length=100)
    blue = models.CharField(max_length=100)
    i_red = models.CharField(max_length=100)
    i_green = models.CharField(max_length=100)
    i_blue = models.CharField(max_length=100)