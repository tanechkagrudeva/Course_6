from django.contrib import admin

from sender.models import Client, Mailing, MailingMessage, MailingLog


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'patronymic', 'email', 'comment',)
    list_filter = ('last_name', 'email',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('time', 'send_period', 'status',)
    list_filter = ('time', 'send_period', 'status',)


@admin.register(MailingMessage)
class MailingMessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'body',)
    list_filter = ('subject', 'body',)


@admin.register(MailingLog)
class MailingLogAdmin(admin.ModelAdmin):
    list_display = ('mailing', 'timestamp', 'status', 'response',)
    list_filter = ('mailing', 'timestamp', 'status', 'response',)