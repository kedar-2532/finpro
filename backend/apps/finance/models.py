from django.db import models

# Create your models here.
class Account(models.Model):
    ACCOUNT_TYPE_CHOICES = (
        ('BANK', 'Bank'),
        ('WALLET', 'Wallet'),
        ('CREDIT', 'Credit'),
    )
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.user.email}"


class Category(models.Model):
    CATEGORY_TYPE_CHOICES = (
        ('INCOME', 'Income'),
        ('EXPENSE', 'Expense'),
    )
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    account_type = models.CharField(max_length=10, choices=CATEGORY_TYPE_CHOICES)

    def __str(self):
        return self.name


class Transaction:
    TRANSACTION_TYPE_CHOICES = (
        ('INCOME', 'Income'),
        ('EXPENSE', 'Expense'),
    )
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.amount}"