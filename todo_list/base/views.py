from django.shortcuts import render
from django.http import HttpResponse


def taskList(request):
    return HttpResponse('This is a task list app')

# Create your views here.
