from django.db import models

class Transaction(models.Model):
    CATEGORY_CHOICES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

    type = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    category = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.type} - {self.category} - {self.amount}"