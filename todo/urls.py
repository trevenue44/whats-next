from django.urls import path
from . import views as todo_views

urlpatterns = [
    path("", todo_views.home, name="todo-home"),
]
