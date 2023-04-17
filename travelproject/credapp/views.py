from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
def login(request):
    if request.method=='POST':
        u_name=request.POST['u_name']
        password=request.POST['password']
        user=auth.authenticate(username=u_name, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials !!")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        u_name = request.POST['username']
        f_name = request.POST['first_name']
        l_name = request.POST['last_name']
        em = request.POST['email']
        passw = request.POST['password']
        cpassw = request.POST['password1']
        if passw==cpassw:
            if User.objects.filter(username=u_name).exists():
                messages.info(request,"User name already taken !!")
                return redirect('register')
            elif User.objects.filter(email=em).exists():
                messages.info(request,"Email already taken !!")
                return redirect('register')
            else:
                user=User.objects.create_user(username=u_name,password=passw,first_name=f_name,last_name=l_name,email=em)
                user.save()
                return redirect('login')

        else:
            messages.info(request,"Passwords not matching !!")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')