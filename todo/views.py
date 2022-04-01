from django.shortcuts import render, redirect
from .models import TODO

# Create your views here.
def index(request):
    todo = TODO.objects.all()
    if request.method == 'POST':
        task_name = request.POST.get('task')
        new_todo = TODO(task_name=task_name)
        new_todo.save()
        return redirect('/')

    return render(request, 'index.html', {'todos':todo})

def delete(request, pk):
    todo = TODO.objects.get(id=pk)
    todo.delete()
    return redirect('/')
