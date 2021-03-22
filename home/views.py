from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from .models import Experience,Supply
from django.contrib.auth import get_user_model
from listvehicle.models import About,Agents
from django.contrib.auth.decorators import login_required
# Create your views here.
@ login_required
def favourite_list(request):
    user = request.user
    favourite_post = user.favourite.all()
    context = {
        'favourite_post' : favourite_post
    }
    return render(request,
                  'home/favourites.html',context)


@ login_required(login_url='/login')
def favourite(request,id):
    supply = get_object_or_404(Supply,id=id)
    if supply.favourite.filter(id=request.user.id).exists():
        supply.favourite.remove(request.user)
    else:
        supply.favourite.add(request.user)
    return HttpResponseRedirect(supply.get_absolute_url())        

def index(request):
    exp = Experience.objects.all()
    supply = Supply.objects.all()
    user = request.user
    sup = Supply.objects.get()
    is_favourite = False
    if sup.favourite.filter(id=request.user.id).exists():
        is_favourite = True

    context = {
        'exp':exp,
        'supply':supply,
        'is_favourite':is_favourite
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
        
