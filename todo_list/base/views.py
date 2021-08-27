from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView, FormView
from .models import Task
from django.urls import reverse_lazy


class TaskList(ListView):
    template_name = "task_list.html"
    model = Task
    context_object_name = "tasks"


# Create your views here.
# class CreateTask(CreateView):
# model = Task
# template_name = "create_task.html"
# context_object_name = "new"


class TaskDetail(DetailView):
    model = Task
    template_name = "task.html"
    context_object_name = "task"


class CreateTask(CreateView):
    model = Task
    template_name = "create_task.html"
    context_object_name = "create"
    fields = "__all__"
    success_url = reverse_lazy('tasks')
