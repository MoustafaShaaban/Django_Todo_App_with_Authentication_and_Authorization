from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("index")
    template_name = "registration/register.html"