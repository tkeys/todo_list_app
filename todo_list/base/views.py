from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView, FormView
from .models import Task
from django.urls import reverse_lazy
from .forms import ContactForm, SignUpForm

from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView


class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class CustomLogoutView(LogoutView):
    template_name = "registration/logout.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


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


class UpdateTask(UpdateView):
    template_name = "update_task.html"
    model = Task
    success_url = reverse_lazy("tasks")
    fields = "__all__"


class DeleteTask(DeleteView):
    template_name = "task_confirm_delete.html"
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy("tasks")


class SignUpView(CreateView):
    template_name = "registration/create_profile.html"
    success_url = reverse_lazy("tasks")
    form_class = SignUpForm

# class ProfileDetail(DetailView):
# template_name = "detail_profile.html"
# model = Profile
# context_object_name = "profile"
