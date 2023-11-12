from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'main/login.html')

@login_required(login_url='login')
def home(request):
    if request.method == "POST":
        name = request.POST['name']
        customer_name = request.POST['customer_name']
        phone_number = request.POST["phone_number"]
        address = request.POST['address']
        if 'completed' in request.POST:
            completed = request.POST['completed']
        else:
            completed = False
        Task.objects.create(name=name, customer_name=customer_name, phone_number=phone_number, address=address, completed=completed)
        return redirect('home')
    return render(request, 'main/home.html')

@login_required(login_url='login')
def completed(request):
    tasks = Task.objects.filter(completed=True)
    context = {"tasks":tasks}
    return render(request, 'main/completed.html', context)

@login_required(login_url='login')
def due(request):
    tasks = Task.objects.filter(completed=False)
    context = {"tasks":tasks}
    return render(request, 'main/due.html', context)

@login_required(login_url='login')
def change_status(request, pk):
    task = Task.objects.get(id=pk)
    if task.completed == False:
        task.completed = True
        task.save()
    else:
        task.completed = False
        task.save()
    return redirect('home')