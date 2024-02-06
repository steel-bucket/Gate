from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import CreateUserForm
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, "home.html")


def logout_view(request):
    logout(request)
    return redirect("/")


def register_staff(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, "Account was created for " + user + " successfully")
            return redirect("staff_login")
    context = {"form": form}
    return render(request, 'users/staff_register.html', context)


def login_staff(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("records")
    context = {}
    return render(request, 'users/staff_login.html')

def records(request):
    if request.method == "GET":
        return render(request, "users/records.html")