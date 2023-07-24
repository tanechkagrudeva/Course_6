from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from sender.models import Client


class ClientListView(ListView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    success_url = reverse_lazy('sender:list')


class ClientUpdateView(UpdateView):
    model = Client
    success_url = reverse_lazy('sender:list')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('sender:list')


class ClientDetailView(DetailView):
    model = Client
    success_url = reverse_lazy('sender:list')