from django.shortcuts import render,redirect
from .models import TaskModel
from .forms import TaskForm
from django.http import Http404

# Create your views here.

def add(request):
    taskForm=TaskForm(request.POST)
    if request.method=="POST":
        if taskForm.is_valid:
            taskForm.save()
            return redirect('add')
        else :
            return render(request,'add.html',{"taskForm":taskForm})
    else:
        return render(request,'add.html',{"taskForm":taskForm})
    

def list(request):
    taskList=TaskModel.objects.all()
    return render(request,'list.html',{"taskList":taskList})

def delete(request,pk):
    try:
        taskList=TaskModel.objects.get(pk=pk)
        taskList.delete()
    except TaskModel.DoesNotExist:
        raise Http404("Task does not exist")
    return redirect('list')

def edit(request,pk):
    try:
        task=TaskModel.objects.get(pk=pk)
        if request.method=="POST":
            taskForm=TaskForm(request.POST,instance=task)
            if taskForm.is_valid():
                taskForm.save()
                return redirect('list')
            else:
                return render(request,'edit.html',{"taskForm":taskForm})
        taskForm=TaskForm(instance=task)
        return render(request,'edit.html',{"taskForm":taskForm})
    except task.DoesNotExist:
        raise Http404("Task does not exist")




def completePage(request):
    taskList=TaskModel.objects.all()
    return render(request,'complete.html',{"taskList":taskList})


def complete(request,pk):
    try:
        taskList=TaskModel.objects.get(pk=pk)
        taskList.is_completed=True
        taskList.save()
    except TaskModel.DoesNotExist:
        raise Http404("Task does not exist")
    return redirect('completePage')


