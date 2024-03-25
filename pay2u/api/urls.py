from django.urls import path

from .views import (
    MainPageView,
    PaymentsView,
    ServicePaymentsView,
    UserSubscriptionView,
    AccountPaymentView,
    AccountView,
    PaymentsPeriodView,
    DocumentView,
    PaymentView,
    CSRFTokenView,
)

urlpatterns = [
    path(
        "v1/users/<int:user_id>/main_page/",
        MainPageView.as_view(),
        name="main_page",
    ),
    path(
        "v1/users/<int:user_id>/payments/",
        PaymentsView.as_view(),
        name="payments",
    ),
    path(
        "v1/users/<int:user_id>/services/<service_id>/payment_history/",
        ServicePaymentsView.as_view(),
        name="service_payments",
    ),
    path(
        "v1/accounts/<int:account_id>/payment_history/",
        AccountPaymentView.as_view(),
        name="account_payments",
    ),
    path(
        "v1/users/account/<int:account_id>/<str:account_status>",
        AccountView.as_view(),
        name="account_view",
    ),
    path(
        "v1/users/<int:user_id>/payment_history/<str:time_period>/",
        PaymentsPeriodView.as_view(),
        name="payments_period",
    ),
    path(
        "v1/users/subscriptions/<int:subscription_id>/",
        UserSubscriptionView.as_view(),
        name="service_payments",
    ),
    path(
        "v1/rules/", DocumentView.as_view(), name="rules"
    ),
    path(
        "v1/payments/<int:payment_id>/",
        PaymentView.as_view(),
        name="payment",
    ),
    path(
        "v1/token/",
        CSRFTokenView.as_view(),
        name="token",
    ),
]
