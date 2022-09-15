from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from item.views import (
    create_checkout_session,
    create_checkout_session_rub,
    ItemDetail,
    SuccessView,
    CancelView,
    ItemsView
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('item', ItemsView, name='items'),
    path('item/<int:pk>/', ItemDetail, name='landing-page'),
    path('buy/<pk>/', create_checkout_session, name='create-checkout-session'),
    path(
        'buy_rub/<pk>/',
        create_checkout_session_rub,
        name='create-checkout-session_rub'
    )
]
