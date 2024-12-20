from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import Todo
from .forms import TodoForm
# Create your views here.
def index(request):
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoForm()

    params={
        "forms": form,
        "list":item_list,
        "title": "ToDo list"
    }

    return render(request, 'index.html', params)

def remove(request, item_id):
   item=Todo.objects.get(id=item_id)
   item.delete()
   messages.info(request, "Item removed !!!")
   return redirect('todo')   