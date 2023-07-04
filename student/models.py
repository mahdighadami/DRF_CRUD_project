from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Student(models.Model):
    SEX_CHOICES = (
        ('male', 'male'),
        ('female', 'female'),
        ('diverse', 'diverse')
    )
    GRADE_CHOICES = (
        ('Associate', 'Associate degree (undergraduate)'),
        ('Bachelor', 'Bachelor\'s degree (undergraduate)'),
        ('Master', 'Master\'s degree (graduate)'),
        ('Doctoral', 'Doctoral degree (graduate)')
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=7, choices=SEX_CHOICES)
    birth_date = models.DateField()
    grade = models.CharField(max_length=9, choices=GRADE_CHOICES)
    register_date = models.DateField(auto_now_add=True)
    graduation_date = models.DateField()
    address = models.TextField()
    phone = PhoneNumberField(null=False, blank=False, unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'