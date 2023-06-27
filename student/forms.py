from django import forms
from phonenumber_field.formfields import PhoneNumberField


# Register Form:
class StudentForm(forms.Form):
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
    first_name = forms.CharField(label="First Name", max_length=50)
    last_name = forms.CharField(label="Last Name", max_length=50)
    phone = PhoneNumberField()
    sex = forms.ChoiceField(label="Sex", choices=SEX_CHOICES)
    grade = forms.ChoiceField(label="Grade", choices=GRADE_CHOICES)

    """The problem with DateTime Fields and their widgets:
    they do not work in HTML !!! """
    # birth_date = forms.DateField(label="Birth", widget=forms.SelectDateWidget(years = range(1970,2010)))
    # register_date = forms.DateTimeField(label="Register Date", widget=forms.SelectDateWidget(years = range(1970,2024)))
    # graduation_date = forms.DateTimeField(label="Graduation Date", widget=forms.SelectDateWidget(years = range(1970,2024)))
    # address = forms.CharField(label="Address", widget=forms.Textarea)
    

# Retrieve Form:
class ReadForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=50)
    last_name = forms.CharField(label="Last Name", max_length=50)
    phone = PhoneNumberField()
