from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField(null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    image=models.ImageField()


    def __str__(self):
        return self.name 

class Car(models.Model):
    car_name=models.CharField(max_length=100)
    speed=models.IntegerField(default=50)

    def __str__(self):
        return self.car_name
    def __len__(self):
        return self.speed 
