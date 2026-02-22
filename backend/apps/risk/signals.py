from django.db.models.signals import post_save
from django.dispatch import receiver
from django.apps import apps
from django.utils import timezone
from datetime import timedelta
from .models import TransactionRisk

Transaction = apps.get_model('transactions',"Transaction")

@receiver(post_save, sender=Transaction)
def calculate_risk(sender, instance, created, **kwargs):
    if not created:
        return
    score = 0
    reason = []
    if instance.amount > 10000:
        score += 50
        reason.append('High Transaction Amount')

    if instance.type == 'DEBIT' and instance.amount >50000:
        score += 40
        reason.append("Large Debit Transaction")

    one_hour_ago = timezone.now() - timedelta(hours=1)
    recent_count = Transaction.objects.filter(user=instance.user,timestamp__gte=one_hour_ago).count()
    if recent_count >5:
        score += 30
        reason.append("High Transaction Frequency")

    flagged = score >= 50

    TransactionRisk.objects.create(
        transaction=instance,
        score=score,
        flagged=flagged,
        reason=", ".join(reason)
    )