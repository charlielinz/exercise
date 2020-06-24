from django.shortcuts import render, redirect
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
        form = AddNewPerson(request.post)

        if form.is_valid():
            form.save()
            text = form.cleaned_data
            form = AddNewPerson
            return redirect('practice:add_detail')
        context = {
            'form': form,
            'text': text
        }
        return render(request, 'practice/add_detail.html', context)
    else:
        form = AddNewPerson()
        context = {
            'form': form
        }
        return render(request, 'practice/add_detail.html', context)
