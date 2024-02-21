from django.db import models

# Create your models here.
class Student(models.Model):
    student_name=models.CharField(max_length=50)
    student_roll=models.IntegerField()
    student_email=models.EmailField()
    student_mobile=models.BigIntegerField()
    def __str__(self):
        return self.student_name
class Course(models.Model):
    course_name=models.CharField(max_length=50)
    course_fee=models.IntegerField()
    course_duration=models.IntegerField()
    def __str__(self):
        return self.course_name
    abc=models.OneToOneField(Student,on_delete=models.CASCADE)