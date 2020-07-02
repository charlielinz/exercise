from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Person
from .forms import AddNewPerson


def index(request):
    persons = Person.objects.all()
    context = {
        'objects': persons,
    }
    return render(request, 'practice/index.html', context)


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


def edit_detail(request, id):
    instance = get_object_or_404(klass=Person, pk=id)
    if request.method == 'POST':
        form = AddNewPerson(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/practice')
        context = {
            'form': form,
        }
        return render(request, 'practice/edit_detail.html', context)

    # """
    # line 46-48
    # form = AddNewPerson(request.POST)
    # if form.is_valid():
    #     name = form.cleaned_data['name']
    #     age = form.cleaned_data['age']
    #     phone_number = form.cleaned_data['phone_number']
    #     email = form.cleaned_data['email']
    # """

    else:
        form = AddNewPerson(instance=instance)
        context = {
            'form': form
        }
        return render(request, 'practice/edit_detail.html', context)


def delete_detail(request, id):
    if request.method == 'POST':
        try:
            person = Person.objects.get(id=id)
        except Person.DoesNotExist:
            raise Http404('Page do not exist')
        person.delete()
        return redirect('/practice')
        context = {
            'person': person
        }
        return render(request, 'practice/delete_detail.html', context)
    else:
        return render(request, 'practice/delete_detail.html')
