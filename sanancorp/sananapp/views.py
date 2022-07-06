from django.views import generic
from django.views.generic.detail import DetailView
from . import models
from django.urls import reverse_lazy

class indexview(generic.ListView):
    model = models.Post
    template_name = 'index.html'

class create_post(generic.edit.CreateView):
    model = models.Post
    template_name = 'create.html'
    fields = '__all__'

class detail(DetailView):
    model = models.Post
    template_name = 'detail.html'

class editview(generic.edit.UpdateView):
    model = models.Post
    template_name = 'edit.html'
    fields = '__all__'

class delete(generic.edit.DeleteView):
    model = models.Post
    success_url = reverse_lazy('createpage')
    template_name = 'delete.html'
