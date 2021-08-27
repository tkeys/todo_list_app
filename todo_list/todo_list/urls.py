"""todo_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from base import views
from base.views import TaskList, TaskDetail, CreateTask, UpdateTask, DeleteTask, SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TaskList.as_view(), name='tasks'),

    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('new/', CreateTask.as_view(), name='new'),
    path('task-update/<int:pk>/', UpdateTask.as_view(), name='update'),
    path('task-delete/<int:pk>/', DeleteTask.as_view(), name='delete'),
    path("sign-up/", SignUpView.as_view(), name="sign-up"),
    #path("profile/<int:pk>", ProfileDetail.as_view(), name="profile"),
]
