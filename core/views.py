from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from blog.models import Article
from sender.models import Mailing, Client


def main_page(request):
    mailing_model = Mailing.objects.all()
    mailing_model_created = Mailing.objects.filter(send_status='created')
    client_model = Client.objects.all()
    articles_model = Article.objects.all()

    context = {
        'mailings': mailing_model,
        'active_mailings': mailing_model_created,
        'clients': client_model,
        'articles': articles_model
    }
    return render(request, 'core/main.html', context)
