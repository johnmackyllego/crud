from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from servers.models import Server
from .forms import ServerForm

# Create your views here.
class ServerList(ListView):
    model = Server
    
class ServerCreate(CreateView):
    model = Server
    success_url = reverse_lazy('server_list')
    form_class = ServerForm
    def get_context_data(self, **kwargs):
        context = super(ServerCreate, self).get_context_data(**kwargs)
        context['a'] = 2
        return context
    
class ServerUpdate(UpdateView):
    model = Server
    success_url = reverse_lazy('server_list')
    form_class = ServerForm
    def get_context_data(self, **kwargs):
        context = super(ServerUpdate, self).get_context_data(**kwargs)
        context['a'] = 1
        return context


class ServerDelete(DeleteView):
    model = Server
    success_url = reverse_lazy('server_list')
