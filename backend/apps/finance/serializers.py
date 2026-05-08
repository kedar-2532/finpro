from rest_framework import serializers
from .models import Account, Category, Transaction, Budget


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
        read_only_fields = ['user', 'balance']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['user']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_fields = ['user']

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError('Amount must be greater than zero.')
        return value

    def validate(self, data):
        request = self.context.get('request')

        if data['account'].user != request.user:
            raise serializers.ValidationError('Invalid account selected.')

        if data['category'].user != request.user:
            raise serializers.ValidationError('Invalid category selected.')

        return data

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'
        read_only_fields = ['user']

    def validate_monthly_limit(self,value):
        if value <= 0:
            raise serializers.ValidationError('Budget limit myst be greater than zero.')
        return value