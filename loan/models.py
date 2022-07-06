
from django.db import models
from accounting.models import CustomUser



class Loan(models.Model):
    LOAN_STATUS = (
        ('C', 'choosing'),
        ('S', 'started'),
        ('R', 'returned'),
        ('T', 'to_be_returned'),
    )
    start_date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey("accounting.CustomUser",on_delete=models.CASCADE,null=True)
    status = models.CharField(max_length=1, choices=LOAN_STATUS, default='C')
    def __str__(self):
        return self.status


class Debt(models.Model):
    amount=models.PositiveIntegerField(null=True,blank=True,default=0)
    def __str__(self):
        return f'{self.amount}'