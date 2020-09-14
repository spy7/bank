from django.shortcuts import render
from decimal import Decimal
from .models import Account
from datetime import date


def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month


def get_interest(value, due_date, paid_interest):
    return (
        value * Decimal(0.1) * Decimal(diff_month(date.today(), due_date) + 1)
    ) - paid_interest


def page_bank(request):
    return render(request, "page.html")


def page_account(request, number):
    if not Account.objects.filter(number=number).exists():
        return render(request, "page.html")
    account = Account.objects.get(number=number)
    sum_debt = account.debt
    if account.debt > 0.005 and date.today() > account.due_date:
        sum_debt += get_interest(
            sum_debt, account.due_date, account.paid_interest
        )
    return render(
        request,
        "account.html",
        context={"account": account, "sum_debt": sum_debt},
    )


def page_credit(request, number):
    if not Account.objects.filter(number=number).exists():
        return render(request, "page.html")
    account = Account.objects.get(number=number)
    sum_debt = account.debt
    interest = 0
    if account.debt > 0.005 and date.today() > account.due_date:
        interest = get_interest(
            sum_debt, account.due_date, account.paid_interest
        )
        sum_debt += interest
    return render(
        request,
        "credit.html",
        context={
            "account": account,
            "sum_debt": sum_debt,
            "interest": interest,
        },
    )
