from django import forms
from .models import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['date_due', 'name', 'amount', 'payer']
        labels = {
            'date_due': 'Date Due',
            'name': 'Expense Name',
            'amount': 'Amount',
            'payer': 'Payer'
        }
        widgets = {
            'date_due': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'payer': forms.TextInput(attrs={'class': 'form-control'})
        }