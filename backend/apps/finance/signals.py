from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from .models import Transaction, Account

@receiver(post_save, sender=Transaction)
def update_account_balance_on_create(sender, instance, created, **kwargs):
    if not created:
        return

    account = instance.account

    if created:
        if instance.transaction_type == 'INCOME':
            account.balance += instance.account
        else:
            account.balance -= instance.account
        account.save()
    print("SIGNAL TRIGGERED:", instance.amount)
@receiver(post_save, sender=Transaction)
def update_account_balance_on_update(sender, instance, **kwargs):
    if not instance.pk:
        return
    old = Transaction.objects.get(pk=instance.pk)
    account = instance.account

    if old.transaction_type == 'INCOME':
        account.balance -= old.amount
    else:
        account.balance += old.amount

    if instance.transaction_type == 'INCOME':
        account.balance += instance.amount
    else:
        account.balance -= instance.amount
    account.save()

@receiver(post_delete, sender=Transaction)
def update_account_balance_on_delete(sender, instance, **kwargs):
    account = instance.account
    if instance.transaction_type == 'INCOME':
        account.balance -= instance.amount
    else:
        account.balance += instance.amount
    account.save()