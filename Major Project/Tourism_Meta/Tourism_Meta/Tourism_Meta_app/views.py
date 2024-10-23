from django.shortcuts import render


def index(request):
    return render(request, 'Home.html')


def gallery(request):
    return render(request, 'Gallery.html')


def AboutUs(request):
    return render(request, 'About Us.html')


def ContactUs(request):
    return render(request, 'Contact Us.html')


def Laksha(request):
    return render(request, 'Lakshadweep.html')


def Ooty(request):
    return render(request, 'Ooty.html')


def Manali(request):
    return render(request, 'Manali.html')


def Coorg(request):
    return render(request, 'Coorg.html')


def Lada(request):
    return render(request, 'Ladakh.html')


def Gate(request):
    return render(request, 'India Gate.html')

# Create your views here.
