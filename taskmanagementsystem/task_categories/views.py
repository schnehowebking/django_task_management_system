from django.shortcuts import render, redirect, get_object_or_404
from .models import TaskCategory
from .forms import TaskCategoryForm

# Create your views here.

def home_categories(request):
    return render(request, 'task_categories/home_categories.html')


def add_category(request):
    if request.method == 'POST':
        form = TaskCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskCategoryForm()
    return render(request, 'task_categories/add_category.html', {'form': form})



def edit_category(request, category_id):
    category = get_object_or_404(TaskCategory, id=category_id)
    if request.method == 'POST':
        form = TaskCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskCategoryForm(instance=category)
    return render(request, 'task_categories/edit_category.html', {'form': form, 'category': category})

def delete_category(request, category_id):
    category = get_object_or_404(TaskCategory, id=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('show_tasks')
    return render(request, 'task_categories/delete_category.html', {'category': category})