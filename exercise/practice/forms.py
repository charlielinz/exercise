from django import forms
from .models import Person


class AddNewPerson(forms.ModelForm):
    name = forms.CharField(max_length=200)
    age = forms.IntegerField()
    phone_number = forms.CharField(max_length=200)
    email = forms.CharField(max_length=200)

    class Meta:
        model = Person
        fields = ['name', 'age', 'phone_number', 'email']
