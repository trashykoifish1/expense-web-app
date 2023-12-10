from django import forms
from .models import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['date_due', 'name', 'payer']
        labels = {
            'date_due': 'Date Due',
            'name': 'Expense Name',
            'payer': 'Payer'
        }
        widgets = {
            'date_due': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'payer': forms.TextInput(attrs={'class': 'form-control'})
        }