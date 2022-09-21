from django.db import models

# Create your models here.
class HomeApp(models.Model):
    home = models.CharField(max_length=255, default='Kerico')
    age = models.IntegerField(default=1)
    salary = models.IntegerField(default=10000)

    def __str__(self):
        return "Home -  " + self.home 