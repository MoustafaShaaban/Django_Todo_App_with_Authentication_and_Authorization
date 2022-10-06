from django.urls import path

from .views import (
    HomePage,
    ListTodo,
    CreateTodo,
    UpdateTodo,
    DeleteTodo,
)


urlpatterns = [
    path('', HomePage.as_view(), name='index'),
    path('todos/', ListTodo.as_view(), name='list-todo'),
    path('todos/create/', CreateTodo.as_view(), name='create-todo'),
    path('todos/update/<int:pk>', UpdateTodo.as_view(), name='update-todo'),
    path('todos/delete/<int:pk>', DeleteTodo.as_view(), name='delete-todo'),
]
