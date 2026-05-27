from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import Account, Category, Transaction, Budget
from .serializers import  AccountSerializer, CategorySerializer, TransactionSerializer, BudgetSerializer
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
        queryset = Transaction.objects.filter(user=self.request.user)

        month = self.request.query_params.get('month')
        year = self.request.query_params.get('year')
        category = self.request.query_params.get('category')
        transaction_type = self.request.query_params.get('transaction_type')

        if month:
            queryset = queryset.filter(date__month=month)

        if year:
            queryset = queryset.filter(date__year=year)

        if category:
            queryset = queryset.filter(category_id=category)

        if transaction_type:
            queryset = queryset.filter(transaction_type=transaction_type)

        return queryset.order_by('-date')

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

class BudgetViewSet(viewsets.ModelViewSet):
    serializer_class = BudgetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class  BudgetSummaryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user = request.user

        budgets = Budget.objects.filter(user=user)
        result = []

        for budget in budgets:
            spent = Transaction.objects.filter(
                user=user,
                category=budget.category,
                transaction_type="EXPENSE",
                # date__month=budget.month,
                # date__year=budget.year
            ).aggregate(total=Sum('amount'))['total'] or 0

            remaining = budget.monthly_limit - spent

            status = "SAFE"
            if spent > budget.monthly_limit:
                status = "OVERSPENT"

            result.append({
                'category': budget.category.name,
                'monthly_limit': float(budget.monthly_limit),
                'spent': float(spent),
                'remaining': float(remaining),
                'status': status
            })
        return Response(result)
    
class AlertsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        user = request.user
        alerts = []
        # Overspent
        budgets = Budget.objects.filter(user=user)
        
        for budget in budgets:
            spent = Transaction.objects.filter(
                user=user,
                category=budget.category,
                transaction_type='EXPENSE',
                date__month=budget.month,
                date__year=budget.year
            ).aggregate(total=Sum('amount'))['total'] or 0
            
            if spent > budget.monthly_limit:
                alerts.append(f"Budget exceeded for {budget.category.name} category")
        # Income/Expense
        income = Transaction.objects.filter(
            user=user,
            transaction_type='INCOME'
        ).aggregate(total=Sum('amount'))['total'] or 0
        
        expense = Transaction.objects.filter(
            user=user,
            transaction_type='EXPENSE'
        ).aggregate(total=Sum("amount"))['total'] or 0
        
        if expense > income:
            alerts.append('Expenses are higher than Income')
        
        if income > 0:
            savings_rate = ((income - expense) / income) * 100
            if savings_rate < 20:
                alerts.append("Savings rate is below safe threshold")
        
        return Response(alerts)

class RiskScoreAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user = request.user

        income = Transaction.objects.filter(
            user=user,
            transaction_type='INCOME'
        ).aggregate(total=Sum('amount'))['total'] or 0

        expense = Transaction.objects.filter(
            user=user,
            transaction_type='EXPENSE'
        ).aggregate(total=Sum('amount'))['total'] or 0

        budget_count = Budget.objects.filter(user=user).count()
        overspent_count = 0

        for budget in Budget.objects.filter(user=user):
            spent = Transaction.objects.filter(
                user=user,
                category=budget.category,
                transaction_type='EXPENSE',
                date__month=budget.month,
                date__year=budget.year
            ).aggregate(total=Sum('amount'))['total'] or 0

            if spent > budget.monthly_limit:
                overspent_count += 1

        risk_score = 0

        if income > 0:
            expense_ratio = (expense / income) * 100
            savings_rate = ((income - expense) / income) * 100
        else:
            expense_ratio = 100
            savings_rate = 0

        if expense_ratio > 80:
            risk_score += 40
        elif expense_ratio > 50:
            risk_score += 25
        elif expense_ratio > 30:
            risk_score += 10

        if budget_count > 0:
            risk_score +=overspent_count * 15

        if savings_rate < 20:
            risk_score += 30
        elif savings_rate <40:
            risk_score += 15

        if risk_score <=25:
            level = 'LOW'
        elif risk_score <=60:
            level = 'MEDIUM'
        else:
            level = 'HIGH'

        data = {
            'risk_score': risk_score,
            'risk_level': level,
            'income': float(income),
            'expense': float(expense),
            'saving_rate': round(float(savings_rate),2)
        }

        return Response(data)

class AIInsightsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user = request.user

        insights = []

        income = Transaction.objects.filter(
            user=user,
            transaction_type="INCOME"
        ).aggregate(total=Sum('amount'))['total'] or 0

        expense = Transaction.objects.filter(
            user=user,
            transaction_type='EXPENSE'
        ).aggregate(total=Sum('amount'))['total'] or 0

        if income > 0:
            savings_rate = ((income - expense) / income) * 100
        else:
            savings_rate = 0

        if savings_rate >= 50:
            insights.append(f"Your savings rate is excellent at {round(savings_rate, 2)}%.")
        elif savings_rate >= 20:
            insights.append(f"Your savings rate is moderate at {round(savings_rate, 2)}%.")
        else:
            insights.append(f"Your savings rate is low at {round(savings_rate, 2)}%.")

        overspent = False

        budgets = Budget.objects.filter(user=user)

        for budget in budgets:
            spent = Transaction.objects.filter(
                user=user,
                category=budget.category,
                transaction_type='EXPENSE',
                date__month=budget.month,
                date__year=budget.year
            ).aggregate(total=Sum('amount'))['total'] or 0

            if spent > budget.monthly_limit:
                overspent = True

        if overspent:
            insights.append('You have exceeded budget limits in some categories.')
        else:
            insights.append('NO budget overspending detected.')

        risk_score = 0

        if income > 0:
            expense_ratio = (expense / income) * 100
        else:
            expense_ratio = 100

        if expense_ratio > 80:
            risk_score += 40
        elif expense_ratio > 50:
            risk_score += 25

        if savings_rate < 20:
            risk_score += 30

        if risk_score <= 25:
            risk_level = 'LOW'
        elif risk_score <= 60:
            risk_level = 'MEDIUM'
        else:
            risk_level = 'HIGH'

        insights.append(f'Your financial risk level is {risk_level}.')

        if income > expense:
            insights.append('Your income flow is healthy.')
        else:
            insights.append('Your expenses are exceeding your income.')

        return Response(insights)