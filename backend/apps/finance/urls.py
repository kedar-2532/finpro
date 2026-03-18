from django.urls import path
from .views import (AccountListCreateView, CategoryListCreateView, TransactionListCreateView)

urlpatterns = [
    path('accounts/', AccountListCreateView.as_view()),
    path('categories/', CategoryListCreateView.as_view()),
    path('transactions/', TransactionListCreateView.as_view()),
]