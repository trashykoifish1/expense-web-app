from django.db import models

# Create your models here.
class Expense(models.Model):
    date_logged = models.DateField(auto_now_add=True)
    date_due = models.DateField()
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    payer = models.CharField(max_length=50)
    paid = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'Expense: {self.name}: ${self.amount} - {self.date_due}'

