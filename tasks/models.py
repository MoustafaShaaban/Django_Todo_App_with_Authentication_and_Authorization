from email.policy import default
from django.db import models
from django.urls import reverse
from users.models import CustomUser


class Todo(models.Model):
	title = models.CharField(max_length=255)
	created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	completed = models.BooleanField(default=False)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('list-todo')