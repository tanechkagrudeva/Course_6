from django.urls import path
from sender.apps import SenderConfig
from sender.views import ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView, ClientDetailView, \
    MailingDetailView, MailingCreateView, MailingUpdateView, MailingDeleteView, MailingListView
from django.views.decorators.cache import cache_page, never_cache

app_name = SenderConfig.name

urlpatterns = [
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('clients/create/', never_cache(ClientCreateView.as_view()), name='client_create'),
    path('clients/update/<int:pk>/', never_cache(ClientUpdateView.as_view()), name='client_update'),
    path('clients/delete/<int:pk>/', never_cache(ClientDeleteView.as_view()), name='client_delete'),
    path('clients/<int:pk>/', cache_page(60)(ClientDetailView.as_view()), name='client_detail'),
    path('mailings/', MailingListView.as_view(), name='mailing_list'),
    path('mailings/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailings/create/', never_cache(MailingCreateView.as_view()), name='mailing_create'),
    path('mailings/update/<int:pk>/', never_cache(MailingUpdateView.as_view()), name='mailing_update'),
    path('mailings/delete/<int:pk>/', never_cache(MailingDeleteView.as_view()), name='mailing_delete'),
]