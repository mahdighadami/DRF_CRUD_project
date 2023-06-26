from django import forms
from phonenumber_field.formfields import PhoneNumberField



class StudentForm(forms.Form):
    SEX_CHOICES = (
        (1, 'male'),
        (2, 'female'),
        (3, 'diverse')
    )
    GRADE_CHOICES = (
        (1, 'Associate degree (undergraduate)'),
        (2, 'Bachelor\'s degree (undergraduate)'),
        (3, 'Master\'s degree (graduate)'),
        (4, 'Doctoral degree (graduate)')
    )
    first_name = forms.CharField(label="First Name", max_length=50)
    last_name = forms.CharField(label="Last Name", max_length=50)
    sex = forms.ChoiceField(label="Sex", choices=SEX_CHOICES)
    grade = forms.ChoiceField(label="Grade", choices=GRADE_CHOICES)
    birth_date = forms.DateTimeField(label="Birth", widget=forms.SelectDateWidget)
    register_date = forms.DateTimeField(label="Register Date", widget=forms.SelectDateWidget)
    graduation_date = forms.DateTimeField(label="Graduation Date", widget=forms.SelectDateWidget)
    address = forms.CharField(label="Address", widget=forms.Textarea)
    phone = PhoneNumberField()


