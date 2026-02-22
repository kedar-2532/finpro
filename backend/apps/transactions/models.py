from django.db import models
from apps.accounts.models import User
# Create your models here.
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    amount = models.DecimalField(max_digits=12,decimal_places=2)
    type = models.CharField(max_length=10,choices=[("CREDIT","Credit"),("DEBIT","Debit")])
    timestamp = models.DateTimeField(auto_now_add=True,db_index=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.type} - {self.amount}"