from django.contrib import admin

from sender.models import Client, Mailing, MailingMessage, MailingLog


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'patronymic', 'email', 'comment',)
    list_filter = ('last_name', 'email',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('time', 'send_period', 'is_active',)
    list_filter = ('time', 'send_period', 'is_active',)


@admin.register(MailingMessage)
class MailingMessageAdmin(admin.ModelAdmin):
    list_display = ('mailing', 'subject', 'body',)
    list_filter = ('mailing', 'subject', 'body',)


@admin.register(MailingLog)
class MailingLogAdmin(admin.ModelAdmin):
    list_display = ('mailing', 'timestamp', 'status', 'response',)
    list_filter = ('mailing', 'timestamp', 'status', 'response',)