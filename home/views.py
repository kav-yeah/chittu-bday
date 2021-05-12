from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home/home.html')

def abiextension(request):
    return render(request,'home/abiextension.html')

def tamilextension(request):
    return render(request,'home/tamilextension.html')

def nikiextension(request):
    return render(request,'home/nikiextension.html')
