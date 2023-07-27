from django.urls import path
from core.apps import CoreConfig
from core.views import main_page

app_name = CoreConfig.name

urlpatterns = [
    path('', main_page, name='contacts'),
]