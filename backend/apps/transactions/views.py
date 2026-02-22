from django.shortcuts import render
from rest_framework import generics,permissions
from .models import Transaction
from .serializers import TransactionSerializer
from apps.accounts.permissions import IsAdmin, IsStaff

# Create your views here.
class TransactionCreateView(generics.CreateAPIView):
    serializer_class = TransactionSerializer
    permission_class = [permissions.IsAuthenticated]

    def perform_create(self,serializer):
        print(self.request.user)
        serializer.save(user=self.request.user)

class TransactionListView(generics.ListAPIView):
    serializer_class = TransactionSerializer
    permission_class = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'ADMIN' or user.role == 'STAFF':
            return Transaction.objects.all().select_related('user').order_by("-timestamp")
        return Transaction.objects.filter(user=user).order_by('-timestamp')