from django.shortcuts import render, redirect
from .models import Transaction
from .forms import TransactionForm
from django.contrib import messages


def index(request):
    transactions = Transaction.objects.all()
    total_income = sum(t.amount for t in transactions if t.type == 'income')
    total_expense = sum(t.amount for t in transactions if t.type == 'expense')
    savings = total_income - total_expense

    context = {
        'transactions': transactions,
        'total_income': total_income,
        'total_expense': total_expense,
        'savings': savings,
    }
    return render(request, 'tracker/index.html', context)

def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transactions = Transaction.objects.all()
            total_income = sum(t.amount for t in transactions if t.type == 'income')
            total_expense = sum(t.amount for t in transactions if t.type == 'expense')
            savings = total_income - total_expense

            # Check if the transaction is an expense and if it will make savings negative
            if transaction.type == 'expense' and transaction.amount > savings:
                messages.error(request, "You don't have enough money to make this transaction. Your savings will go negative!")
                return render(request, 'tracker/add_transaction.html', {'form': form})

            transaction.save()
            messages.success(request, "Transaction added successfully!")
            return redirect('index')
    else:
        form = TransactionForm()
    return render(request, 'tracker/add_transaction.html', {'form': form})


def reset_transactions(request):
    # Delete all transactions
    Transaction.objects.all().delete()
    messages.success(request, "All transactions have been reset. Income, expenses, and savings are now zero.")
    return redirect('index')