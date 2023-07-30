from django.db import models
from users.models import User
from datetime import date, datetime

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='имя')
    last_name = models.CharField(max_length=50, verbose_name='фамилия')
    patronymic = models.CharField(max_length=50, verbose_name='отчество')

    email = models.EmailField(max_length=150, verbose_name='почта')
    comment = models.TextField(verbose_name='комментарий')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='активный')

    def __str__(self):
        return f'{self.first_name} ({self.email})'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class MailingMessage(models.Model):
    subject = models.CharField(max_length=255, verbose_name='тема')
    body = models.TextField(verbose_name='текст письма')
    client = models.ManyToManyField(Client, verbose_name='клиент', blank=True, null=True, )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', blank=True, null=True,)
    created_at = models.DateTimeField(default=datetime.now, verbose_name='создано')

    def __str__(self):
        return f'{self.subject} {self.client}'

    class Meta:
        verbose_name = 'письмо'
        verbose_name_plural = 'письма'


class Mailing(models.Model):
    ONCE = 'разовая'
    DAILY = 'ежедневно'
    WEEKLY = 'еженедельно'
    MONTHLY = 'ежемесячно'

    SEND_PERIOD = [
        (ONCE, 'разовая'),
        (DAILY, 'ежедневно'),
        (WEEKLY, 'еженедельно'),
        (MONTHLY, 'ежемесячно'),
    ]

    CREATED = 'создана'
    COMPLETED = 'завершена'
    LAUNCHED = 'запущена'

    SELECT_STATUS = [
        (CREATED, 'создана'),
        (COMPLETED, 'завершена'),
        (LAUNCHED, 'запущена'),
    ]

    message = models.ForeignKey(MailingMessage, default=1, on_delete=models.CASCADE, verbose_name='сообщение')
    time = models.TimeField(default=datetime.now, verbose_name='время')
    start = models.DateTimeField(default=datetime.now, verbose_name='начало рассылки')
    finish = models.DateTimeField(default=datetime.now, verbose_name='окончание рассылки')
    send_period = models.CharField(max_length=150, choices=SEND_PERIOD, verbose_name='периодичность')
    status = models.CharField(max_length=100, default='начало рассылки', choices=SELECT_STATUS, verbose_name='статус')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, **NULLABLE, verbose_name='создана')


    def __str__(self):
        return f'{self.time} - {self.send_period} - {self.status}'

    class Meta:
        verbose_name = 'настройка'
        verbose_name_plural = 'настройки'


class MailingLog(models.Model):
    DELIVERED = 'delivered'
    NOT_DELIVERED = 'not_delivered'

    STATUS = (
        (DELIVERED, 'доставлено'),
        (NOT_DELIVERED, 'не доставлено'),
    )

    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='настройка')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='дата последней рассылки')
    status = models.CharField(choices=STATUS, max_length=255, verbose_name='статус')
    response = models.TextField(**NULLABLE, verbose_name='ответ сервера')

    def __str__(self):
        return f'{self.timestamp} - {self.status}'

    class Meta:
        verbose_name = 'попытка'
        verbose_name_plural = 'попытки'
