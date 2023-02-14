from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib import messages
from django.contrib import auth

def SignUp(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if CustomUser.objects.filter(email=email).exists():
            messages.error('This email has already been taken')           
        elif password == password2:
            user =   CustomUser.objects.create(email=email, password=password, password2=password2)
            user.save()
            messages.success(request, 'Your account has been made')
            return redirect('/') 
        else:
            messages.error(request, 'Your passwords do not match')
          
    else:
        return render(request, 'users/signup.html')

def SignIn(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, f'Welcome back')
            return('/')

        else:
            messages.error('Your password or username are not correct')

    else:
        return render(request, 'users/signin.html')
