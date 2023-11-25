from django.db import models

# Create your models here.
class Jobs(models.Model):
    job_role=models.CharField(max_length=100)
    experience=models.IntegerField()
    SalaryCTC=models.IntegerField()
    company=models.CharField(max_length=100)
    location=models.CharField(max_length=100)

    def __str__(self):
        return self.job_role