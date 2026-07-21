from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        'name' : 'amir'
    }
    return render(request,'mymodule/index.html', context)

def show_user(request, user):
    return HttpResponse(f'hello {user}')