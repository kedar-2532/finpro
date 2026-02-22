from django.db import models
from apps.accounts.models import User
# Create your models here.
class TransactionRisk(models.Model):
    transaction = models.OneToOneField('transactions.Transaction',
                                       on_delete = models.CASCADE,
                                       related_name = 'risk',
                                       db_index = True
                                       )
    score = models.IntegerField()
    flagged = models.BooleanField(default=False)
    reason = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Risk {self.score} - {self.transaction.id}"