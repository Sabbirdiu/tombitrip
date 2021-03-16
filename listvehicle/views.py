from django.shortcuts import render
from .models import Videos
# Create your views here.
def listvehicle(request):
    videos = Videos.objects.all()
    context ={
        'videos':videos,
    }
    return render(request,'listvehicle/listvehicle.html',context)

  