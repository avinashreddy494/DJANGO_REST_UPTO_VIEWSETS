from django.db import models

# Create your models here.
class Instructor(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()

    def __str__(self):
        return self.name
    
class stacks(models.Model):
    stack_name=models.CharField(max_length=100)
    rating=models.FloatField()
    Instructor=models.ForeignKey(Instructor,on_delete=models.CASCADE,related_name='stacks')

    def __str__(self):
        return self.stack_name