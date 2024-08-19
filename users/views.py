from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

# Create your views here.

def home_view(request):
    return render(request, 'index.html')

def register_view(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password2 != password:
            return render(request, 'register.html', context={"message_password": 'Error password !!'})
        else:
            if User.objects.filter(username=username).exists():
                return render(request, 'register.html', context={"message": 'username already exists !!'})
            new_users = User(first_name=first_name, last_name=last_name, email=email, username=username)
            new_users.set_password(password)
            new_users.save()
            return redirect('login')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('index')

        else:
            return render(request, 'login.html', context={'message': "username or password invalid"})
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

class UserLoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        user_from = AuthenticationForm(data=request.POST)
        if user_from.is_valid():
            user = user_from.get_user()
            login(request, user)
            messages.success(request, 'welcome')
            return render(request, 'register.html')
class UserRegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password2']
        if password1 == password2:
            new_user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                email=email)
            new_user.set_password(password1)
            new_user.save()
            messages.success(request, "You successfully registered")
            return redirect('login')
        else:
            messages.warning(request, "Passwords don't match")
            return render(request, 'register.html')

class UserLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "You have been successfully logged out.")
        return redirect('login')
