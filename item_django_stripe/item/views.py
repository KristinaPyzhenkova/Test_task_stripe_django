import requests
import stripe
from django.conf import settings
from django.views.generic import TemplateView
from django.shortcuts import redirect, get_object_or_404, render

from .models import Item

data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"


def ItemsView(request):
    products = Item.objects.all()
    context = {'products': products}
    return render(request, 'list_item.html', context)


def ItemDetail(request, pk):
    product = get_object_or_404(Item, pk=pk)
    context = {
        "product": product
    }
    return render(request, 'detail_item.html', context)


def create_checkout_session(request, pk):
    product = get_object_or_404(Item, pk=pk)
    YOUR_DOMAIN = "http://158.160.4.33"
    if product.currency == 'usd':
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': int(product.price) * 100,
                        'product_data': {
                            'name': product.name
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                "product_id": product.id
            },
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )

        return redirect(checkout_session.url, code=303)
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': (
                        int(
                            int(product.price) / data['Valute']['USD']['Value']
                        ) * 100
                    ),
                    'product_data': {
                        'name': product.name
                    },
                },
                'quantity': 1,
            },
        ],
        metadata={
            "product_id": product.id
        },
        mode='payment',
        success_url=YOUR_DOMAIN + '/success/',
        cancel_url=YOUR_DOMAIN + '/cancel/',
    )

    return redirect(checkout_session.url, code=303)


def create_checkout_session_rub(request, pk):
    product = get_object_or_404(Item, pk=pk)
    YOUR_DOMAIN = "http://158.160.4.33"
    if product.currency == 'usd':
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'rub',
                        'unit_amount': (
                            int(product.price) * int(
                                data['Valute']['USD']['Value'] * 100
                            )
                        ),
                        'product_data': {
                            'name': product.name
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                "product_id": product.id
            },
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )

        return redirect(checkout_session.url, code=303)
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'rub',
                    'unit_amount': int(product.price) * 100,
                    'product_data': {
                        'name': product.name
                    },
                },
                'quantity': 1,
            },
        ],
        metadata={
            "product_id": product.id
        },
        mode='payment',
        success_url=YOUR_DOMAIN + '/success/',
        cancel_url=YOUR_DOMAIN + '/cancel/',
    )
    return redirect(checkout_session.url, code=303)
