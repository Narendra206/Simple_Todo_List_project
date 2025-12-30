from django.shortcuts import render, redirect
from .models import Task

# Create your views here.

from django.shortcuts import render, redirect
from .models import Task

def index(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        Task.objects.create(title=task)
        return redirect('/')
    
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def delete_task(request, task_id):
    Task.objects.get(id=task_id).delete()
    return redirect('/')

def mark_complete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('/')
