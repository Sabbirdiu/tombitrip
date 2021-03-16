from django.shortcuts import render

# Create your views here.
def listvehicle(request):
    return render(request,'listvehicle/listvehicle.html')