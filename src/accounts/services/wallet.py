from django.db import transaction
from django.db.models import F

from accounts.models import Wallet
from commons.messages.error_messages import ErrorMessages
from transactions.services.transaction import TransactionService


class WalletService:
    repository = Wallet
    transaction_service = TransactionService()

    @classmethod
    @transaction.atomic
    def deposit(cls, *, wallet_id: int, value: float):
        cls.repository.objects.select_for_update().filter(id=wallet_id).update(balance=F('balance') + value)

    @classmethod
    @transaction.atomic
    def withdraw(cls, *, wallet_id: int, value: float):
        wallet = cls.repository.objects.select_for_update().filter(id=wallet_id).first()
        if not cls.check_balance(wallet, value):
            raise ValueError(ErrorMessages.INSUFFICIENT_BALANCE.message)
        wallet.balance = F('balance') - value
        wallet.save(update_fields=['balance'])

    @classmethod
    def check_balance(cls, wallet, amount: float) -> bool:
        return wallet.balance >= amount
