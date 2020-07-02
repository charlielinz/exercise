from django import forms
from .models import Person


class AddNewPerson(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age', 'phone_number', 'email']
