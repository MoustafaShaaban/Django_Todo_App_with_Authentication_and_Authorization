from django.db import models
from django.urls import reverse
from users.models import CustomUser
from django.contrib.auth.models import User


class Todo(models.Model):
	title = models.CharField(max_length=255)
	created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('list-todo')