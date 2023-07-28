from django.forms import modelformset_factory
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from sender.forms import ClientForm, MailingMessageForm
from sender.models import Client, MailingMessage
from sender.services import send_mailing


class ClientListView(ListView):
    model = Client

    def get_queryset(self):
        return Client.objects.filter(user=self.request.user.pk)


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('sender:client_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        product_formset = modelformset_factory(Client, form=ClientForm, extra=1)
        context_data['title'] = 'Добавить товар'
        if self.request.method == 'POST':
            context_data['formset'] = product_formset(self.request.POST)
        else:
            context_data['formset'] = product_formset()
        return context_data

    def form_valid(self, form):
        mailing = form.save()
        mailing.user = self.request.user
        mailing.save()
        return super().form_valid(form)


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('sender:client_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        client_formset = modelformset_factory(Client, form=ClientForm, extra=1)
        context_data['title'] = 'Добавить товар'
        if self.request.method == 'POST':
            context_data['formset'] = client_formset(self.request.POST)
        else:
            context_data['formset'] = client_formset()
        return context_data


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('sender:client_list')


class ClientDetailView(DetailView):
    model = Client
    success_url = reverse_lazy('sender:client_list')


class MailingListView(ListView):
    model = MailingMessage

    def get_queryset(self):
        return MailingMessage.objects.filter(user=self.request.user.pk)


class MailingCreateView(CreateView):
    model = MailingMessage
    form_class = MailingMessageForm
    success_url = reverse_lazy('sender:mailing_list')

    def form_valid(self, form):
        mailing = form.save()
        mailing.user = self.request.user
        mailing.save()
        send_mailing(mailing)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        mailing_message_formset = modelformset_factory(MailingMessage, form=MailingMessageForm, extra=1)
        context_data['title'] = 'Добавить рассылку'
        if self.request.method == 'POST':
            context_data['formset'] = mailing_message_formset(self.request.POST)
        else:
            context_data['formset'] = mailing_message_formset()
        return context_data


class MailingUpdateView(UpdateView):
    model = MailingMessage
    form_class = MailingMessageForm
    success_url = reverse_lazy('sender:mailing_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        mailing_message_formset = modelformset_factory(MailingMessage, form=MailingMessageForm, extra=1)
        context_data['title'] = 'Редактировать рассылку'
        if self.request.method == 'POST':
            context_data['formset'] = mailing_message_formset(self.request.POST)
        else:
            context_data['formset'] = mailing_message_formset()
        return context_data


class MailingDeleteView(DeleteView):
    model = MailingMessage
    success_url = reverse_lazy('sender:mailing_list')


class MailingDetailView(DetailView):
    model = MailingMessage
    success_url = reverse_lazy('sender:mailing_list')


