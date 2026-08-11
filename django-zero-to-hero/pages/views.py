from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse('hello there')


def about(request):
    return HttpResponse('About Up Page')