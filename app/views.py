from django.shortcuts import render, redirect
from .models import Appointment, Doctor, News, Contact
from django.contrib import messages

def HomePage(request):
    doctor = Doctor.objects.all()
    news = News.objects.all()
    context = {
        'doctors' : doctor,
        'news' : news
    }

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        date = request.POST.get('date')
        department = request.POST.get('department')
        number = request.POST.get('number')
        message = request.POST.get('message')

        appointment =   Appointment.objects.create(full_name=full_name, email=email, date=date, department=department, number=number, message=message)
        appointment.save()
        messages.success(request, 'Your appointment has been made')
        return redirect('/')
    
    else:
        return render(request, 'app/index.html', context)

def AboutPage(request):
    doctor = Doctor.objects.all()
    context = {
        'doctors' : doctor
    }

    return render(request, 'app/about.html', context)

def DoctorPage(request):
    doctor = Doctor.objects.all()
    context = {
        'doctors' : doctor
    }

    return render(request, 'app/doctors.html', context)


def NewsPage(request):
    news = News.objects.all()

    context = {
        'news' : news
    }

    return render(request, 'app/blog.html', context)

def DetailPage(request, slug ):
    news = News.objects.get(slug = slug)
    new = News.objects.all()
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        website = request.POST.get('website')
        message = request.POST.get('message')

        contact =   Contact.objects.create(name=name, email=email,website=website ,message=message)
        contact.save()
        messages.success(request, 'Your appointment has been made')
        return redirect("You'll recieve a response in an email from us in 1-2 business days")

    context = {
        'news' : news,
        'new' : new
    }
    return render(request, 'app/blog-detail.html', context)

def ContactPage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact =   Contact.objects.create(name=name, email=email,subject=subject ,message=message)
        contact.save()
        messages.success(request, 'Your appointment has been made')
        return redirect("You'll recieve a response in an email from us in 1-2 business days")
    
    else:
        return render(request, 'app/contact.html')
