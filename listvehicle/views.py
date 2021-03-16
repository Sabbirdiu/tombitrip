from django.shortcuts import render
from .models import Videos,About
# Create your views here.
def listvehicle(request):
    videos = Videos.objects.all()
    about = About.objects.get()
    context ={
        'videos':videos,
        'about':about
    }
    return render(request,'listvehicle/listvehicle.html',context)

  