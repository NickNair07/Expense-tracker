from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from accounts.models import CustomUser


class Expense(models.Model):

    CATEGORIES = [
        ('Food', 'Food'), 
        ('Transportation', 'Transportation'), 
        ('Entertainment', 'Entertainment'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=255, help_text="e.g., 'Lunch at McDonald's'")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=50, choices=CATEGORIES, default='Food')

    def __str__(self):
        return self.description

    def clean(self):
        # Custom validation for the amount field
        if self.amount <= 0:
            raise ValidationError("Amount must be greater than zero.")

        # Custom validation for the date field
        if self.date > timezone.now().date():
            raise ValidationError("Date cannot be in the future.")