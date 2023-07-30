from django.core.mail import send_mail
from sender.models import Client, MailingLog, Mailing, MailingMessage
from config import settings


def send_email(*args):
    all_email = []
    for client in Client.objects.all():
        all_email.append(str(client.email))

    for mailing in Mailing.objects.all():
        if mailing.status == Mailing.CREATED and mailing.send_period == (str(*args)):
            filtered_message = mailing.message
            message = MailingMessage.objects.filter(subject=filtered_message)
            for m in message:
                send_mail(
                    subject=m.subject,
                    message=m.body,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[*all_email],
                )
                status_list = []
                server_response = {
                    'sending': Mailing.objects.get(pk=mailing.id),
                    'status': MailingLog.DELIVERED,
                    'response': [*all_email]}
                status_list.append(MailingLog(**server_response))
                MailingLog.objects.bulk_create(status_list)
                if mailing.periodicity == Mailing.ONCE:
                    mailing.status = Mailing.COMPLETED
                    mailing.save()
                else:
                    mailing.status = Mailing.LAUNCHED
                    mailing.save()


