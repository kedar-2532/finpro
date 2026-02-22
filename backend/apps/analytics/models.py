from django.db import models
from apps.accounts.models import User
# Create your models here.

class UserStats(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    total_credit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_debit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    last_transaction_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} stats"