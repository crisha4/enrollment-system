from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Custom fields
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    suffix = models.CharField(max_length=10, blank=True, null=True)
    contact_number = models.CharField(max_length=15)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    address = models.TextField()
    student_type = models.CharField(max_length=20, choices=[
        ('regular', 'Regular'),
        ('irregular', 'Irregular'),
        ('transferee', 'Transferee'),
        ('new', 'New Student'),
    ])
    course = models.CharField(max_length=10, choices=[('BSCS', 'BSCS'), ('BSIT', 'BSIT')])
    year_level = models.IntegerField(choices=[(1, '1st Year'), (2, '2nd Year'), (3, '3rd Year'), (4, '4th Year')])
    student_id = models.CharField(max_length=20, unique=True)
