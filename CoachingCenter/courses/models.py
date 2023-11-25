from django.db import models

# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=100)
    Price=models.IntegerField()
    Discount=models.IntegerField()
    Duration=models.CharField(max_length=100)
    Auhorname=models.CharField(max_length=100)

    def __str__(self):
        return self.name