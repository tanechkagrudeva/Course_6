from django.core.management import BaseCommand

from sender.services import mailing_processing


class Command(BaseCommand):

    def handle(self, *args, **options):
        mailing_processing()