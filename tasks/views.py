from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from accounts.models import CustomUser


# List Tasks
def tasksList(request):
    user = request.user
    tasks = Task.objects.filter(user=user)

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            saving = form.save(commit=False)
            saving.user = request.user
            saving.save()
        return redirect('tasks')

    context = {
        'tasks': tasks,
        'form': form,
    }
    return render(request, 'tasks/list_tasks.html', context)


"""
def createtodo(request):
    if request.method == 'GET':
        return render(request, 'todo/createtodo.html', {'form': TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'todo/createtodo.html', {
                'form': TodoForm(),
                'error': 'Bad data passed in. Try again.'
            })
"""


# Update Task
def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('tasks')
    context = {'form': form}
    return render(request, 'tasks/update_task.html', context)


# Delete Task
def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('tasks')

    context = {'item': item}
    return render(request, 'tasks/delete.html', context)
