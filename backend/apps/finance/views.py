from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import Account, Category, Transaction
from .serializers import  AccountSerializer, CategorySerializer, TransactionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from django.db.models.functions import ExtractMonth
# Create your views here.

class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DashboardAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user = request.user

        accounts = Account.objects.filter(user=user)
        transactions = Transaction.objects.filter(user=user)

        total_balance = accounts.aggregate(total=Sum('balance'))['total'] or 0

        total_income = transactions.filter(
            transaction_type = 'INCOME'
        ).aggregate(total=Sum('amount'))['total'] or 0
        total_expense = transactions.filter(
            transaction_type='EXPENSE'
        ).aggregate(total=Sum('amount'))['total'] or 0

        recent_transactions = transactions.order_by('-date')[:5]

        data = {
            "total_balance": total_balance,
            "total_income": total_income,
            "total_expense": total_expense,
            "recent_transactions": [
                {
                    "id": t.id,
                    "amount": t.amount,
                    "type": t.transaction_type,
                    "date": t.date
                } for t in recent_transactions
            ]
        }

        return Response(data)

class MonthlySummaryAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        user = request.user
        transactions = Transaction.objects.filter(user=user).annotate(
            month = ExtractMonth('date')
        )

        summary = {}

        for t in transactions:
            month = t.month

            if month not in summary:
                summary[month] = {
                    "month":month,
                    "income":0,
                    "expense":0
                }

            if t.transaction_type == 'INCOME':
                summary[month]['income'] += float(t.amount)
            else:
                summary[month]['expense'] += float(t.amount)

        return Response(list(summary.values()))

class CategorySummaryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user = request.user
        transactions = Transaction.objects.filter(user=user)
        summary = {}

        for t in transactions:
            key = t.category.name

            if key not in summary:
                summary[key] = {
                    "category": t.category.name,
                    "type": t.category.category_type,
                    "total": 0
                }
            summary[key]['total'] += float(t.amount)
        return Response(list(summary.values()))

class IncomeExpenseChartAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user = request.user

        transactions = Transaction.objects.filter(user=user)
        income = transactions.filter(
            transaction_type = "INCOME"
        ).aggregate(total=Sum('amount'))['total'] or 0

        expense = transactions.filter(
            transaction_type = "EXPENSE"
        ).aggregate(total=Sum('amount'))['total'] or 0

        data = {
            "income": float(income),
            "expense": float(expense),
            "net_savings": float(income - expense)
        }
        return Response(data)