from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Todo
from users.models import CustomUser


class HomePage(TemplateView):
	template_name = 'index.html'


class ListTodo(LoginRequiredMixin, ListView):
	model = Todo
	template_name = 'todos/todo_list.html'
	context_object_name = 'todos'
	paginate_by = 3

	def get_queryset(self):
		return Todo.objects.filter(created_by=self.request.user)



class CreateTodo(LoginRequiredMixin, CreateView):
	model = Todo
	fields = ['title']
	template_name = 'todos/create_todo.html'

	def form_valid(self, form):
		form.instance.created_by = self.request.user
		return super().form_valid(form)


class UpdateTodo(LoginRequiredMixin, UpdateView):
	model = Todo
	fields = ['title']
	template_name = 'todos/update_todo.html'
	success_url = reverse_lazy('list-todo')


class DeleteTodo(LoginRequiredMixin, DeleteView):
	model = Todo
	template_name = 'todos/delete_todo.html'
	success_url = reverse_lazy('list-todo')
