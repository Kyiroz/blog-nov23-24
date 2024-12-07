from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy #Al enviar un formulario, te devolvera a una parte en especifico

# Create your views here.

class SignUpView(CreateView):

    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = 'registration/signup.html'