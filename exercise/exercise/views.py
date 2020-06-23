from django.shortcuts import render


def index(request):
    profile = {'Name': 'Charlie'}
    return render(request, 'practice/index.html', profile)


def info(request):
    info = {'Age': 'age: 27', 'Phone_number': 'phone number: 0983097997', 'Email': 'email: ilovealinlin@gmail.com'}
    return render(request, 'practice/info.html', info)
