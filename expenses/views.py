from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from datetime import datetime
import calendar
from django.shortcuts import redirect
from .models import Expense
from .forms import ExpenseForm

# Create your views here.
def index(request):
    today = datetime.now()
    current_month = today.month
    month = calendar.month_name[current_month]
    all = Expense.objects.all()
    expenses = []
    for expense in all:
        if expense.date_due.month == current_month:
            expenses.append(expense) 
    return render(request, 'expenses/index.html', {
        'expenses': expenses,
        'month': month
    })

def view_expense(request, id):
    expense = Expense.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def toggle_status(request, id):
    expense = Expense.objects.get(pk=id)
    if expense.paid:
        expense.paid = False
    else:
        expense.paid = True
    expense.save()
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            new_date_due = form.cleaned_data['date_due']
            new_name = form.cleaned_data['name']
            new_payer = form.cleaned_data['payer']

            new_expense = Expense(
                date_due = new_date_due,
                name = new_name,
                payer = new_payer
            )
            new_expense.save()
            return render(request, 'expenses/add.html', {
                'form': ExpenseForm(),
                'success': True
            })
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add.html', {
        'form': ExpenseForm()
    })