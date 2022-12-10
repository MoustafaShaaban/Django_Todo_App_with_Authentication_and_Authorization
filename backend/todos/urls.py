from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomePage.as_view(), name='index'),
    path('todos/', views.ListTodo.as_view(), name='list-todo'),
    path('todos/create/', views.CreateTodo.as_view(), name='create-todo'),
    path('todos/update/<int:pk>', views.UpdateTodo.as_view(), name='update-todo'),
    path('todos/delete/<int:pk>', views.DeleteTodo.as_view(), name='delete-todo'),
]
