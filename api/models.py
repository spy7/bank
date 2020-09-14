from django.db import models
from datetime import date


class Account(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    paid_interest = models.DecimalField(
        max_digits=10, decimal_places=2, default=0
    )
    due_date = models.DateField(default=date.today)

    class Meta:
        db_table = "account"

    def __str__(self):
        return f"{self.number}: {self.name}"


class Extract(models.Model):
    date = models.DateField(default=date.today)
    description = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    account = models.ForeignKey(
        Account, on_delete=models.PROTECT, related_name="extracts",
    )

    class Meta:
        db_table = "extract"


class Credit(models.Model):
    date = models.DateField(default=date.today)
    description = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_interest = models.BooleanField()
    account = models.ForeignKey(
        Account, on_delete=models.PROTECT, related_name="credits",
    )

    class Meta:
        db_table = "credit"
