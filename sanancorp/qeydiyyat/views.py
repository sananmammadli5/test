from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

class Signup(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('indexpage')
    template_name = 'signup.html'
