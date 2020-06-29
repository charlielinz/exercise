from django.shortcuts import render, redirect
from django.http import Http404
from .models import Person
from .forms import AddNewPerson


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
    if request.method == 'POST':
        form = AddNewPerson(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/practice')
        context = {
            'form': form,
        }
        return render(request, 'practice/add_detail.html', context)

    else:
        form = AddNewPerson()
        context = {
            'form': form
        }
        return render(request, 'practice/add_detail.html', context)


def edit_detail(request):
    context = {

    }
    return render(request, 'practice/edit_detail.html', context)


def delete_detail(request, id):
    try:
        person = Person.objects.get(id=id)
    except Person.DoesNotExist:
        raise Http404('Page do not exist')
    person.delete()
    context = {
        'person': person
    }
    return render(request, 'practice/delete_detail.html', context)
