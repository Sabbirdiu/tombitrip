from django.shortcuts import render
from .models import Experience
# Create your views here.
def index(request):
    exp = Experience.objects.all()
    context = {
        'exp':exp
    }
    return render(request,'home/home.html',context)