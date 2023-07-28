import schedule
from django.core.cache import cache
from django.core.mail import send_mail
from django.utils import timezone
from sender.models import Client, MailingLog, Mailing, MailingMessage
from config import settings
from datetime import timedelta, datetime
import logging


def send_mailing():
    """Рассылка"""
    messages = MailingMessage.objects.all()
    for message in messages:
        current_time = timezone.now()
        mailing = message.mailing.send_period


