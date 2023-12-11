from django.shortcuts import render, redirect, get_object_or_404
from .models import TaskModel
from .forms import TaskForm

# Create your views here.

def index(request):
    return render(request, 'tasks/index.html')


def show_tasks(request):
    tasks = TaskModel.objects.all()
    return render(request, 'tasks/show_tasks.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})

def edit_task(request, task_id):
    task = get_object_or_404(TaskModel, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(TaskModel, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('show_tasks')
    return render(request, 'tasks/delete_task.html', {'task': task})

def task_details(request, task_id):
    task = get_object_or_404(TaskModel, id=task_id)
    return render(request, 'tasks/task_details.html', {'task': task})

def save_completed_status(request, task_id):
    task = get_object_or_404(TaskModel, id=task_id)
    if request.method == 'POST':
        task.is_completed = request.POST.get('is_completed') == 'on'
        task.save()
    return redirect('show_tasks')