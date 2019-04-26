from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        username = input('Введите имя пользователя: ')
        email = input('Введите адрес электронной почты: ')
        password = input('Введите пароль: ')
        password2 = input('Повторите ввод пароля: ')
        while password != password2:
            password2 = input('Пароли не совпадают, повторите ввод пароля еще раз: ')
        User.objects.create_superuser(username=username,
                                      email=email,
                                      password=password)
        self.stdout.write(f'Пользователь {username} создан')

