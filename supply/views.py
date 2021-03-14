from django.shortcuts import render

# Create your views here.
def supply(request):
    return render(request,'supply/supply.html')