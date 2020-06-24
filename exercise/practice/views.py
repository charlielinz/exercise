from django.shortcuts import render
from .models import Person


def index(request):
    persons = Person.objects.all()
    context = {
        'objects': persons,
    }
    return render(request, 'practice/index.html', context)


def persons_detail(request, id):
    person = Person.objects.get(id=id)
    context = {
        'object': person,
    }
    return render(request, 'practice/persons_detail.html', context)


def add_detail(request):
    context = {

    }
    return render(request, 'practice/add_detail.html', context)
