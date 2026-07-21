from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse("Home Page")

def show_user(request, user):
    return HttpResponse(f'hello {user}')