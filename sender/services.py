from django.core.cache import cache
from django.core.mail import send_mail
from django.utils import timezone
from sender.models import Client, MailingLog, Mailing, MailingMessage
from config import settings
from datetime import timedelta, datetime
import logging


def send_mailing(mailing):
    current_time = timezone.now()
    emails = [client.email for client in mailing.client.all()]
    send_mail(mailing.subject,
              mailing.body,
              settings.EMAIL_HOST_USER,
              emails)



