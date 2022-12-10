from email.policy import default
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Todo(models.Model):
	title = models.CharField(max_length=255)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE)
	completed = models.BooleanField(default=False)

	class Meta:
		verbose_name = 'todo'
		verbose_name_plural = 'todos'

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('list-todo')
