from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class student(models.Model):
    SEX_CHOICES = (
        ('m', 'male'),
        ('f', 'female'),
        ('d', 'diverse')
    )
    GRADE_CHOICES = (
        ('a', 'Associate degree (undergraduate)'),
        ('b', 'Bachelor\'s degree (undergraduate)'),
        ('m', 'Master\'s degree (graduate)'),
        ('d', 'Doctoral degree (graduate)')
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    birth_date = models.DateTimeField()
    grade = models.CharField(max_length=1, choices=GRADE_CHOICES)
    register_date = models.DateTimeField(auto_now_add=True)
    graduation_date = models.DateTimeField()
    address = models.TextField()
    phone = PhoneNumberField(null=False, blank=False, unique=True)
