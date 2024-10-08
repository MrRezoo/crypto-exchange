from django.contrib.auth import get_user_model
from django.db import models

from commons.models import BaseModel
from exchanges.models.crypto_currency import CryptoCurrency
from orders.enums import OrderStates

User = get_user_model()


class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    crypto = models.ForeignKey(CryptoCurrency, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=10, decimal_places=8)  # 8 equal to 0.00000001 1 satoshi
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    state = models.CharField(max_length=10, choices=OrderStates.choices, default=OrderStates.PENDING)
    is_aggregated = models.BooleanField(default=False)

    class Meta:
        indexes = [
            models.Index(fields=['is_aggregated']),
            models.Index(fields=['state']),
        ]
