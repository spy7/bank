from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Extract


@receiver(post_save, sender=Extract)
def update_account(sender, instance=None, created=False, **kwargs):
    if created and instance.account:
        account = instance.account
        account.balance += instance.value
        account.save()
