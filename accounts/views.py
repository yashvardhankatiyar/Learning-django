from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register(request):
    if request.method == 'GET' :
        return render(request, 'register.html')
    
    
    username = request.POST['username']
    email = request.POST['email']
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']

    if password1 != password2 :
        messages.error(request, "passwords are not matching")
        return redirect("register")
    
    if User.objects.filter(username = username).exists() : 
        messages.error(request, "Username already taken")
        return redirect("register")

    if User.objects.filter(email = email).exists() : 
        messages.error(request, "email already register")
        return redirect("register")

    user = User.objects.create_user(
        username=username,
        email = email,
        password = password1,
        first_name = first_name,
        last_name = last_name
    )

    user.save()

    messages.success(request, "Account created successfully !")
    return redirect("login")


def loginReq(request) : 
    
    if request.method == "GET" :
        return render(request, "login.html")
    
    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(request, username = username, password = password)

    if user is not None :
        login(request, user)
        return redirect("home")
    
    else :
        messages.error(request, "no user found ! register !!")
        return redirect("login")

def logoutReq(request) :
    logout(request)
    return redirect("home")