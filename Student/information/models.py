from django.db import models

# Create your models here.


class Student(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField(default=0,blank=True)
    school=models.CharField(max_length=50)
    description=models.TextField()

    def __str__(self):
        return self.name

