from django.db import models


class itemDetails(models.Model):
    student_id = models.IntegerField()
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    age = models.IntegerField()
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=100, null=True)
    qualifications = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to="image/", null=True)


class teacherDetails(models.Model):
    teacher_id = models.IntegerField()
    nname = models.CharField(max_length=100, null=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=100, null=True)
    position = models.CharField(max_length=100, null=True)
    phone = models.IntegerField()
    email = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to="image/", null=True)


# Create your models here.
from django.db import models

# Create your models here.
