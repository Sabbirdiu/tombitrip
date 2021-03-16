from django.shortcuts import render
from .models import Videos,About,Agents
# Create your views here.
def listvehicle(request):
    videos = Videos.objects.all()
    about = About.objects.get()
    context ={
        'videos':videos,
        'about':about
    }
    return render(request,'listvehicle/listvehicle.html',context)

def agents(request):
    agents = Agents.objects.all()  
    context ={
        'agents':agents,
       }
    return render(request,'listvehicle/agents.html',context)