from django.shortcuts import render
from .models import vuses, Faculty

# Create your views here.
def index(request):
    con = {
        "model": vuses
    }
    return render(request, 'lifecourse/index.html', context = con)

def vusreg(request):
    return render(request, 'lifecourse/vusregistration.html')
def get_groups_by_department(request):
    return render(request, 'lifecourse/vusregistration.html')
def add_group(request):
    return render(request, 'lifecourse/vusregistration.html')

def getvusprofile(request, vusname):
    print(vusname)
    vus = vuses.objects.get(name = vusname)

    print(vus.name)
    return render(request, 'lifecourse/vusprofile.html', context={vus})
