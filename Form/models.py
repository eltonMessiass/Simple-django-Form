from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class College(models.Model):
    name = models.CharField(max_length=2000)
    course = models.OneToOneField(Course, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name



class University(models.Model):
    name = models.CharField(max_length=2000)
    college = models.OneToOneField(College, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name



class Student(models.Model):
    university = models.OneToOneField(University, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    email = models.EmailField(max_length=1000, null=False)
    
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


