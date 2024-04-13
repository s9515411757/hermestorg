# Generated by Django 5.0.3 on 2024-04-13 08:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_favourites_follow_follow_user_and_author_unique_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='follow',
            options={'verbose_name': 'Подписка', 'verbose_name_plural': 'Подписки'},
        ),
        migrations.AddField(
            model_name='favourites',
            name='flag',
            field=models.BooleanField(default=False, help_text='Активна избранное или нет', verbose_name='Активен'),
        ),
        migrations.AddField(
            model_name='follow',
            name='flag',
            field=models.BooleanField(default=False, help_text='Активна подписка или нет', verbose_name='Активен'),
        ),
        migrations.AlterField(
            model_name='favourites',
            name='card',
            field=models.ForeignKey(help_text='Добавьте продукт', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='favouriting', to='products.card', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='favourites',
            name='user',
            field=models.ForeignKey(help_text='Выбирите пользователя', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='favouriter', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
