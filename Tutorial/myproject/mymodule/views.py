from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'name' : 'amir'
    }
    return render(request,'mymodule/index.html', context)


def about(request):
    return render(request, 'mymodule/about.html')

def contact(request):
    return render(request, 'mymodule/contact.html')