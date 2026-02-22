from django.db.models.signals import post_save
from django.dispatch import receiver
from django.apps import apps
from django.utils import timezone
from .models import UserStats

Transaction = apps.get_model('transactions','Transaction')

@receiver(post_save, sender=Transaction)
def update_user_stats(sender,instance,created,**kwargs):
    if created:
        user = instance.user
        stats, _ = UserStats.objects.get_or_create(user=user)

        if instance.type == 'CREDIT':
            stats.total_credit += instance.amount
        elif instance.type == "DEBIT":
            stats.total_debit += instance.amount

        stats.last_transaction_date = timezone.now()
        stats.save()