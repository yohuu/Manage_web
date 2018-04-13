from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)
    birthday = models.DateField()

class Project(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    deadline = models.DateField()
    progress = models.CharField(max_length=50)
    budget = models.IntegerField()
    description = models.TextField()
    leader = models.ForeignKey(Student)

class Module(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    deadline = models.DateField()
    description = models.TextField()
    student = models.ForeignKey(Student)
    project = models.ForeignKey(Project)
