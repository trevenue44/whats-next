from django.urls import path
from . import views as todo_views

urlpatterns = [
    path("", todo_views.home, name="todo-home"),
    path("add-todo-item/", todo_views.add_todo_item, name="add-todo-item"),
    path(
        "delete-todo-item/<int:todo_item_id>/",
        todo_views.delete_todo_item,
        name="delete-todo-item",
    ),
]
