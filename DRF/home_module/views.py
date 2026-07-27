from django.shortcuts import render
from todo_module.models import Todo
from django.http import JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

def home_page(request):
    todos = Todo.objects.all()
    return render(request, "home_module/home_page.html", {
        "todos" : todos
    })
    
    
@api_view(['GET'])
def todos_json(request: Request):
    todos = list(Todo.objects.all().values('title', 'is_done'))
    return Response({
        'todos':todos},
        status.HTTP_200_OK
    )