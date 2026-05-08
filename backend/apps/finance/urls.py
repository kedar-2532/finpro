from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AccountViewSet, CategoryViewSet, TransactionViewSet, DashboardAPIView, MonthlySummaryAPIView, CategorySummaryAPIView, IncomeExpenseChartAPIView, BudgetViewSet, BudgetSummaryAPIView, AlertsAPIView, RiskScoreAPIView, AIInsightsAPIView

router = DefaultRouter()
router.register('accounts', AccountViewSet, basename='accounts')
router.register('categories', CategoryViewSet, basename='categories')
router.register('transactions', TransactionViewSet, basename='transactions')
router.register('budgets', BudgetViewSet, basename='budgets')
urlpatterns = router.urls

urlpatterns += [
    path('dashboard/', DashboardAPIView.as_view()),
    path('monthly-summary/', MonthlySummaryAPIView.as_view(), name='monthly-summary'),
    path('category-summary/', CategorySummaryAPIView.as_view(), name='category-summary'),
    path('income-expense-chart/', IncomeExpenseChartAPIView.as_view(), name='income-expense-chart'),
    path('budget-summary/', BudgetSummaryAPIView.as_view(), name='budget-summary'),
    path('alerts/', AlertsAPIView.as_view(), name='alerts'),
    path('risk-score/', RiskScoreAPIView.as_view(), name='risk-score'),
    path('ai-insights/', AIInsightsAPIView.as_view(), name='ai-insights'),
]