from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'first_name', 'middle_name', 'last_name', 'suffix',
            'email', 'contact_number', 'dob', 'gender', 'address',
            'student_type', 'course', 'year_level', 'student_id'
        ]
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'middle_name': forms.TextInput(attrs={'placeholder': 'Middle Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'suffix': forms.TextInput(attrs={'placeholder': 'Suffix (e.g., Jr., Sr., III)'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'contact_number': forms.TextInput(attrs={'placeholder': 'Contact Number'}),
            'address': forms.TextInput(attrs={'placeholder': 'Address'}),
            'student_id': forms.TextInput(attrs={'placeholder': 'Student ID'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Custom choices for dropdown fields
        self.fields['gender'].choices = [('male', 'Male'), ('female', 'Female')]
        self.fields['student_type'].choices = [
            ('regular', 'Regular'),
            ('irregular', 'Irregular'),
            ('transferee', 'Transferee'),
            ('new', 'New Student')
        ]
        self.fields['course'].choices = [
            ('BSCS', 'BSCS'),
            ('BSIT', 'BSIT')
        ]
        self.fields['year_level'].choices = [
            (1, '1st Year'),
            (2, '2nd Year'),
            (3, '3rd Year'),
            (4, '4th Year')
        ]
