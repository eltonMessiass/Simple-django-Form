
from .models import Student, University, College
from django import forms


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'email', 'university']

class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = ['college']

class CollegeForm(forms.ModelForm):
    class Meta:
        model = College
        fields = ['course']