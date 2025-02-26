from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Recipe(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    recipe_name=models.CharField(max_length=100)
    recipe_description=models.TextField()
    recipe_image=models.ImageField(upload_to='recipe')
    recipe_view_count=models.IntegerField(default=1)


    def __str__(self):
        return self.recipe_name 

class Department(models.Model):
    department=models.CharField(max_length=100)
    def __str__(self):
        return self.department 
    class Meta:
        ordering=['department']

class StudentId(models.Model):
    student_id=models.CharField(max_length=100)
    def __str__(self):
        return self.student_id 
class Student(models.Model):
    department=models.ForeignKey(Department,related_name='depart',on_delete=models.CASCADE)
    student_id=models.OneToOneField(StudentId,related_name='studentid',on_delete=models.CASCADE)
    student_name=models.CharField(max_length=100)
    student_email=models.EmailField(unique=True)
    student_age=models.IntegerField(default=18)
    student_address=models.TextField()
    def __str__(self):
        return self.student_name

    class Meta:
        ordering=['student_name']
        verbose_name='student'


#Models for student report card project 
class Subject(models.Model):
    subject_name=models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name



class SubjectMarks(models.Model):
    student=models.ForeignKey(Student,related_name='studentmarks',on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    marks=models.IntegerField()

    class Meta:
        unique_together=['student','subject']

    def __str__(self):
        return f'{self.student.student_name} {self.subject.subject_name}'

class ReportCard(models.Model):
    student=models.ForeignKey(Student,related_name='studentreportcard',on_delete=models.CASCADE)
    student_rank=models.IntegerField()
    date_of_report_card_generation=models.DateField(auto_now_add=True)

    class Meta:
        unique_together=['student_rank','date_of_report_card_generation']