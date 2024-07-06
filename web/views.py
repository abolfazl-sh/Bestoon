from django.shortcuts import render
from json import JSONEncoder
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from web.models import Token, User, Expense, Income
from datetime import datetime
# Create your views here.

@csrf_exempt
def submit_expense(request):
    this_token = request.POST['token']
    user = User.objects.filter(token__token=this_token).get()
    now = datetime.now()
    Expense.objects.create(user=user, amount=request.POST['amount'], date=now, text=request.POST['text'])
    print("I submit expense")

    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)

@csrf_exempt
def submit_income(request):
    this_token = request.POST['token']
    user = User.objects.filter(token__token=this_token).get()
    now = datetime.now()
    Income.objects.create(user=user, amount=request.POST['amount'], date=now, text=request.POST['text'])
    print("I submit income")

    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)

