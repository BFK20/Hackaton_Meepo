from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'lifecourse/base.html')

def vusreg(request):
    return render(request, 'lifecourse/vusregistration.html')

