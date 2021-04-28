from django.db import models
from django.db.models.base import Model

# Create your models here.
class Carrer(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=50)
    duration = models.PositiveSmallIntegerField(default=5)

class Student(models.Model):
    dni = models.CharField(max_length=8, primary_key=True)
    first_last_name = models.CharField(max_length=35)
    second_last_name = models.CharField(max_length=35)
    name = models.CharField(max_length=35)
    date_of_birth = models.DateField()
    sexes = [
        ('F', 'Female'),
        ('M', 'Male')
    ]
    sex = models.CharField(max_length=1, choices=sexes, default = 'F')
    career = models.ForeignKey(Carrer, null=False, blank=False, on_delete=models.CASCADE)
    vigencia = models.BooleanField(default=True)

    def full_name(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.first_last_name, self.second_last_name, self.name)


class Course(models.Model):
    code = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=30)
    credits = models.PositiveSmallIntegerField()
    teacher = models.CharField(max_length=100)

class enrollment(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, null=False, blank=False, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=False, blank=False, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
