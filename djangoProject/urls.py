
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('todo_list_project.tasks.urls')),
    path('', lambda request: redirect('task-list')),
]
