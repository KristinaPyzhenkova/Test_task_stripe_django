# Test_task_stripe_django

![workflow](https://github.com/KristinaPyzhenkova/Test_task_stripe_django/actions/workflows/main.yml/badge.svg)

Проект развернут по адресу: http://158.160.4.33/item

Данные для авторизации в админке:
Username: Test
email: test@mail.ru
password: test

## Описание проекта.
Проект Test_task_stripe_django: веб-сайт, на котором размещены товары (в доллорах и рублях - около price обозначена валюта). Товары можно просмотреть (детально и список) и оплатить данные товары(так же в разной валюте). Проект был развернут на Яндекс.Облако.

Стек технологий:
```
Django, Stripe, Docker.
```

## Как запустить проект: 
Пересобрать контейнер и запустить контейнер:
```
docker-compose up -d --build
```
Выполнить миграции:
```
docker-compose exec web python manage.py migrate
```
Создать суперпользователя:
```
docker-compose exec web python manage.py createsuperuser
```
Cобрать статику:
```
docker-compose exec web python manage.py collectstatic --no-input
```
Проект доступен по адресу:
```
http://localhost/
```
