from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q

from .utils import download_csv
from .models import Task
from .forms import TaskForm


@login_required
def index_view(request):
    tasks = Task.objects.all()
    context = {
        'Tasks': tasks,
    }
    return render(request, 'index.html', context)


@login_required
def detail_view(request, task_id):
    try:
        tasks = Task.objects.get(pk=task_id)
        context = {
            'Tasks': tasks,
        }
    except Task.DoesNotExist:
        raise Http404("Task not found.")
    return render(request, 'detail.html', context)


@login_required
def create_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = TaskForm(request.POST)
            new_task.save()
            messages.success(request, 'Tasks added successfully.')
            return redirect('task:index')
    else:
        form = TaskForm()
    return render(request, 'forms.html', {'form': form})


@login_required
def update_view(request, task_id):
    try:
        tasks = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404("Task not found.")
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
            messages.success(request, f'Task {task_id} edited.')
            return redirect('task:index')
    else:
        form = TaskForm(instance=tasks)
    return render(request, 'forms.html', {'form': form})


@login_required
def delete_view(request, task_id):
    try:
        tasks = Task.objects.get(pk=task_id)
        tasks.delete()
        messages.success(request, f'Task {task_id} Deleted Successfully')
        return redirect('task:index')
    except Task.DoesNotExist:
        raise Http404("Task not found.")


@login_required
def to_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    data = download_csv(request, Task.objects.all())
    return HttpResponse(data, content_type='text/csv')


@login_required
def search(request):
    results = []
    if request.method == "GET":
        query = request.GET.get('search')
        if query == '':
            query = 'None'
        results = Task.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    return render(request, 'search.html', {'query': query, 'results': results})
