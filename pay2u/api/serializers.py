from rest_framework import serializers

from subscriptions.models import Subscription, UserSubscription, TrialPeriod
from services.models import Service
from payments.models import Payment, CashbackApplied
from users.models import Account


class TrialPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrialPeriod
        fields = ("period_cost", "period_days")


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ("id", "image", "name")


class SubscriptionSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True, source="service_id")
    trial = TrialPeriodSerializer(read_only=True, source="trial_period")

    class Meta:
        model = Subscription
        fields = ("name", "price", "period", "cashback", "service", "trial")


class MainPageSerializer(serializers.ModelSerializer):
    subscription = SubscriptionSerializer(read_only=True)

    class Meta:
        model = UserSubscription
        fields = (
            "id",
            "status",
            "activation",
            "renewal",
            "start",
            "end",
            "trial",
            "subscription",
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        subscription_data = {"user_subscription": data}
        return subscription_data


class PaymentsAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("id", "account_number")


class CashbackAppliedSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashbackApplied
        fields = ("id", "amount", "applied_status")


class PaymentsSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(
        read_only=True, source="user_subscription.service_id"
    )
    account = PaymentsAccountSerializer(read_only=True, source="account_id")
    cashback = CashbackAppliedSerializer(
        read_only=True, source="cashback_applied"
    )

    class Meta:
        model = Payment
        fields = (
            "id",
            "date",
            "amount",
            "service",
            "account",
            "cashback",
        )
