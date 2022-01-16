from re import template
from django.urls import path
from . import views as todo_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", login_required(todo_views.TodoItemListView.as_view()), name="todo-home"),
    path("add-todo-item/", todo_views.add_todo_item, name="add-todo-item"),
    path(
        "delete-todo-item/<int:todo_item_id>/",
        todo_views.delete_todo_item,
        name="delete-todo-item",
    ),
]
