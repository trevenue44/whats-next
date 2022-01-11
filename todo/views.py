from django.shortcuts import redirect, render
from .models import TodoItem


def home(request):
    context = {
        "todo_items": TodoItem.objects.all(),
    }
    return render(request, "todo/home.html", context=context)


def add_todo_item(request):
    content = request.POST["content"]
    new_todo_item = TodoItem(content=content)
    new_todo_item.save()
    return redirect("todo-home")


def delete_todo_item(request, todo_item_id):
    todo_item = TodoItem(id=todo_item_id)
    todo_item.delete()
    return redirect("todo-home")
