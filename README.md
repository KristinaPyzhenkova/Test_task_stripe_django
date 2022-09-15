# Test_task_stripe_django

![workflow](https://github.com/KristinaPyzhenkova/Test_task_stripe_django/actions/workflows/main.yml/badge.svg)

Проект развернут по адресу: http://158.160.4.33/item

Данные для авторизации в админке:
Username: Test
email: test@mail.ru
password: test

## Описание проекта.
Проект foodgram-project-react сервис, на котором пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

Данный проект реализован на библиотеке djangorestframework.

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
