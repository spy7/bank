from django.db import models


class Account(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "account"

    def __str__(self):
        return f"{self.number}: {self.name}"


class Extract(models.Model):
    description = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    account = models.ForeignKey(
        Account,
        on_delete=models.PROTECT,
        related_name="extracts",
    )

    class Meta:
        db_table = "extract"
