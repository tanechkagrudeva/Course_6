# Generated by Django 4.2.3 on 2023-07-10 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='фамилия')),
                ('patronymic', models.CharField(max_length=50, verbose_name='отчество')),
                ('email', models.EmailField(max_length=150, verbose_name='почта')),
                ('comment', models.TextField()),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'клиенты',
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_time', models.TimeField(verbose_name='время рассылки')),
                ('send_period', models.CharField(choices=[('daily', 'Раз в день'), ('weekly', 'Раз в неделю'), ('monthly', 'Раз в месяц')], max_length=7, verbose_name='периодичность')),
                ('send_status', models.CharField(choices=[('created', 'Создана'), ('started', 'Запущена'), ('completed', 'Завершена')], max_length=9, verbose_name='статус')),
            ],
            options={
                'verbose_name': 'настройка',
                'verbose_name_plural': 'настройки',
            },
        ),
        migrations.CreateModel(
            name='MailingMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255, verbose_name='тема')),
                ('body', models.TextField(verbose_name='текст письма')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sender.mailing', verbose_name='настройка')),
            ],
            options={
                'verbose_name': 'рассылка',
                'verbose_name_plural': 'рассылки',
            },
        ),
        migrations.CreateModel(
            name='MailingLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='дата пследней рассылки')),
                ('status', models.CharField(max_length=255, verbose_name='статус')),
                ('response', models.TextField(blank=True, null=True, verbose_name='ответ сервера')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sender.mailing', verbose_name='настройка')),
            ],
            options={
                'verbose_name': 'попытка',
                'verbose_name_plural': 'попытки',
            },
        ),
    ]