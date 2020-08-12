from django.shortcuts import render
from .models import Account


def page_bank(request):
    return render(request, 'page.html')


def page_account(request, number):
    if not Account.objects.filter(number=number).exists():
        return render(request, 'page.html')
    account = Account.objects.get(number=number)
    return render(request, 'account.html', context={"account": account})
