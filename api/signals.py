from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Extract, Credit
from dateutil.relativedelta import relativedelta


@receiver(post_save, sender=Extract)
def update_account(sender, instance=None, created=False, **kwargs):
    if created and instance.account:
        account = instance.account
        account.balance += instance.value
        account.save()


@receiver(post_save, sender=Credit)
def update_credit(sender, instance=None, created=False, **kwargs):
    if created and instance.account:
        account = instance.account
        if instance.is_interest:
            account.paid_interest -= instance.value
        else:
            if instance.value < 0 or account.debt < 0.01:
                account.due_date = instance.date + relativedelta(months=+1)
            account.debt += instance.value
            if account.debt < 0.01:
                account.paid_interest = 0
        account.save()
