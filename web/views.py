from django.shortcuts import render
from json import JSONEncoder
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from web.models import Token, User, Expense, Income
from datetime import datetime
from django.contrib.auth import get_user_model
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

def logout(request):
    context = {}
    return render(request, 'logout.html', context)

@csrf_exempt
def login(request):
    
    context = {}
    if "username" in request.POST:
        username = request.POST["username"] if "username" in request.POST else ""
        email = request.POST["email"] if "email" in request.POST else ""
        password = request.POST["password"] if "password" in request.POST else ""
        newuser = User.objects.create(username=username, password=password, email=email)
        newuser.save()
        return render(request, 'login.html', context)
    elif "email" in request.POST:
        this_email = request.POST["email"] if "email" in request.POST else ""
        this_password = request.POST["password"] if "password" in request.POST else ""
        if User.objects.filter(email=this_email) and User.objects.filter(password=this_password):
            return render(request, 'home.html', context)
    else:
        return render(request, 'login.html', context)

@csrf_exempt
def signup(request):
    context = {}
    return render(request, 'signup.html', context)

def home(request):
    context = {}
    return render(request, 'home.html', context)