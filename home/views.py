from django.shortcuts import render,get_object_or_404
from .models import Experience
# Create your views here.
def index(request):
    exp = Experience.objects.all()
    context = {
        'exp':exp
    }
    return render(request,'home/home.html',context)
def exp_details(request,slug):
    exp = get_object_or_404(Experience,slug=slug) 

    context = {
        'exp':exp
    }
    return render(request,'home/details.html',context)
        