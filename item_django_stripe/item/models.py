from django.db import models


class Item(models.Model):
    USD = 'usd'
    RUB = 'rub'
    CURRENCY_CHOICES = [
        (USD, 'доллар'),
        (RUB, 'рубль'),
    ]

    name = models.CharField(
        max_length=25,
        verbose_name='Название',
        db_index=True
    )
    description = models.CharField(
        max_length=250,
        verbose_name='Описание',
        db_index=True
    )
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        verbose_name='Стоимость',
    )
    currency = models.CharField(
        max_length=7,
        choices=CURRENCY_CHOICES,
        verbose_name='Валюта'
    )

    def __str__(self):
        return self.name
