from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from .models import Experience,Supply,Rating,CommentForm
from django.contrib.auth import get_user_model
from listvehicle.models import About,Agents
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
    return HttpResponseRedirect('/favourites')        

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
def supply(request):
    supply = Supply.objects.all()
    sup = Supply.objects.get()
    is_favourite = False
    if sup.favourite.filter(id=request.user.id).exists():
        is_favourite = True
    context = {
        'supply' :supply,
        'is_favourite':is_favourite
    }    
    return render(request,'home/supply.html',context)    
def supply_details(request,slug,id):
    supply = Supply.objects.get(pk=id,slug=slug)
    comments = Rating.objects.filter(supply_id=id,status='True')

    context ={
        'supply':supply,
        'comments':comments
    }
    return render(request,'home/supply_details.html',context)    

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
        
def addcomment(request,id):
   url = request.META.get('HTTP_REFERER')  # get last url
   #return HttpResponse(url)
   if request.method == 'POST':  # check post
      form = CommentForm(request.POST)
      if form.is_valid():
         data = Rating()  # create relation with model
         data.subject = form.cleaned_data['subject']
         data.comment = form.cleaned_data['comment']
         data.rate = form.cleaned_data['rate']
         data.ip = request.META.get('REMOTE_ADDR')
         data.supply_id=id
         current_user= request.user
         data.user_id=current_user.id
         data.save()  # save data to table
         messages.success(request, "Your review has ben sent. Thank you for your interest.")
         return HttpResponseRedirect(url)

   return HttpResponseRedirect(url)  