from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Data, DjangoD, Flutter_Developer, Redu, Software
from home.models import Fullstack
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'index.html')
    


def Profile(request):
    return render(request, 'Profile.html')


def feedback(request):
    return render(request, 'feedback.html')


def FullstackDeveloper(request):
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        if not Fullstack.objects.filter(name=name, email=email, phone=phone, desc=desc, date=datetime.today()).exists():
            FullstackDeveloper = Fullstack.objects.create(
                name=name, email=email, phone=phone, desc=desc, date=datetime.today())
            FullstackDeveloper.save()
            messages.success(
                request, 'Your Application has been submitted, Thanks for your Interest')
        else:
            messages.success(request, 'You previously applied for Job')
    return render(request, 'FullstackDeveloper.html')


def Redux(request):
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        if not Redu.objects.filter(name=name, email=email, phone=phone, desc=desc, date=datetime.today()).exists():
            Redux = Redu(name=name, email=email, phone=phone,
                         desc=desc, date=datetime.today())
            Redux.save()
            messages.success(
                request, 'Your Application has been submitted, Thanks for your Interest')
        else:
            messages.success(request, 'You previously applied for Job')
    return render(request, 'Redux.html')


def SoftwareDeveloper(request):
   
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        if not Software.objects.filter(name=name, email=email, phone=phone, desc=desc, date=datetime.today()).exists():
            SoftwareDeveloper = Software(
                name=name, email=email, phone=phone, desc=desc, date=datetime.today())
            SoftwareDeveloper.save()
            messages.success(
                request, 'Your Application has been submitted, Thanks for your Interest')
        else:
            messages.success(request, 'You previously applied for Job')
    return render(request, 'SoftwareDeveloper.html')


def DjangoDeveloper(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        if not DjangoD.objects.filter(name=name, email=email, phone=phone, desc=desc, date=datetime.today()).exists():
            DjangoDeveloper = DjangoD(
                name=name, email=email, phone=phone, desc=desc, date=datetime.today())
            DjangoDeveloper.save()
            messages.success(
                request, 'Your Application has been submitted, Thanks for your Interest')
        else:
            messages.success(request, 'You previously applied for Job')
    return render(request, 'DjangoDeveloper.html')


def FlutterDeveloper(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        if not Flutter_Developer.objects.filter(name=name, email=email, phone=phone, desc=desc, date=datetime.today()).exists():
            FlutterDeveloper = Flutter_Developer(
                name=name, email=email, phone=phone, desc=desc, date=datetime.today())
            FlutterDeveloper.save()
            messages.success(
                request, 'Your Application has been submitted, Thanks for your Interest')
        else:
            messages.success(request, 'You previously applied for Job')
    return render(request, 'FlutterDeveloper.html')


def DataScientist(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        if not Data.objects.filter(name=name, email=email, phone=phone, desc=desc, date=datetime.today()).exists():
            DataScientist = Data(name=name, email=email,
                                 phone=phone, desc=desc, date=datetime.today())
            DataScientist.save()
            messages.success(
                request, 'Your Application has been submitted, Thanks for your Interest',)
        else:
            messages.success(request, 'You previously applied for Job')
    return render(request, 'DataScientist.html')
