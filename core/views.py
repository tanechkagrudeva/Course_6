from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from blog.models import Article
from sender.models import Mailing, Client, MailingMessage


@login_required()
def main_page(request):
    mailing_model = MailingMessage.objects.all().filter(user=request.user.pk)
    mailing_model_created = Mailing.objects.all().filter(send_status='created')
    client_model = Client.objects.filter(user=request.user.pk)
    articles_model = Article.objects.all()

    context = {
        'mailings': mailing_model,
        'active_mailings': mailing_model_created,
        'clients': client_model,
        'articles': articles_model
    }
    return render(request, 'core/main.html', context)
