from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=48)
    
    def __str__(self):
        return f"{str(self.user).title()}_token"



class Expense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.date} - {self.amount}"

class Income(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.date} - {self.amount}"