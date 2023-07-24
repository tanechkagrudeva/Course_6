from django.urls import path
from sender.apps import SenderConfig
from sender.views import ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView, ClientDetailView

app_name = SenderConfig.name

urlpatterns = [
    path('clients/', ClientListView.as_view(), name='list'),
    path('clients/create/', ClientCreateView.as_view(), name='create'),
    path('clients/update/<int:pk>/', ClientUpdateView.as_view(), name='update'),
    path('clients/delete/<int:pk>/', ClientDeleteView.as_view(), name='delete'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client_detail')
]