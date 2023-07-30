import django
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms import modelformset_factory
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from sender.forms import ClientForm, MailingMessageForm
from sender.models import Client, MailingMessage, Mailing
from sender.services import send_email


class ClientListView(LoginRequiredMixin, ListView):
    model = Client

    def get_queryset(self):
        return Client.objects.filter(user=self.request.user.pk)


class ClientCreateView(LoginRequiredMixin, CreateView):
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


class ClientUpdateView(LoginRequiredMixin, UpdateView):
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


class ClientDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Client
    permission_required = 'sender.delete_client'
    success_url = reverse_lazy('sender:client_list')



class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    success_url = reverse_lazy('sender:client_list')


class MailingListView(LoginRequiredMixin, ListView):
    model = MailingMessage

    def get_queryset(self):
        return MailingMessage.objects.filter(user=self.request.user.pk)


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = MailingMessage
    form_class = MailingMessageForm
    success_url = reverse_lazy('sender:mailing_list')
    try:
        for mailing in Mailing.objects.all():
            if mailing.status == Mailing.CREATED:
                send_email(Mailing.ONCE)
    except django.db.utils.ProgrammingError:
        print('ProgrammingError')

    def form_valid(self, form):
        mailing = form.save()
        mailing.user = self.request.user
        mailing.save()
        send_email(mailing)

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


class MailingUpdateView(LoginRequiredMixin, UpdateView):
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


class MailingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = MailingMessage
    permission_required = 'sender.delete_mailing'
    success_url = reverse_lazy('sender:mailing_list')


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = MailingMessage
    success_url = reverse_lazy('sender:mailing_list')


