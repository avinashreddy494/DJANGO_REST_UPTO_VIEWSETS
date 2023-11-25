from django.db import models

# Create your models here.


class admission(models.Model):
    student_name=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=100)
    stack=models.CharField(max_length=100)

    def __str__(self):
        return self.student_name+str("-")+str(self.stack)