from django.shortcuts import render,get_object_or_404
from .models import Experience
from listvehicle.models import About,Agents
# Create your views here.
def index(request):
    exp = Experience.objects.all()
    context = {
        'exp':exp
    }
    return render(request,'home/home.html',context)
def exp_details(request,slug):
    exp = get_object_or_404(Experience,slug=slug) 
    about = About.objects.get()
    agents = Agents.objects.all()  
    context = {
        'exp':exp,
        'about':about,
        'agents':agents,
    }
    return render(request,'home/details.html',context)
        