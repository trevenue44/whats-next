from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import TodoItem


# @login_required()
# def home(request):
#     context = {
#         "todo_items": TodoItem.objects.all(),
#     }
#     return render(request, "todo/home.html", context=context)


class TodoItemListView(ListView):
    model = TodoItem
    template_name = "todo/home.html"  # <app_name>_<viewtype>.html
    context_object_name = "todo_items"

    def get_queryset(self):
        return TodoItem.objects.filter(author=self.request.user)


@login_required()
def add_todo_item(request):
    content = request.POST["content"]
    if content:
        new_todo_item = TodoItem(content=content, author=request.user)
        new_todo_item.save()
    return redirect("todo-home")


@login_required()
def delete_todo_item(request, todo_item_id):
    todo_item = TodoItem(id=todo_item_id)
    todo_item.delete()
    return redirect("todo-home")
