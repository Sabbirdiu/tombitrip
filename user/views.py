from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.
def signup_form(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save() #completed sign up
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            # Create data in profile table for user
            # current_user = request.user
            # data=UserProfile()
            # data.user_id=current_user.id
            # data.image="images/users/user.png"
            # data.save()
            messages.success(request, 'Your account has been created!')
            return HttpResponseRedirect('/login')
        else:
            messages.warning(request,form.errors)
            return HttpResponseRedirect('/login')


    form = SignUpForm()
   
    context = {
               'form': form,
               }
    return render(request, 'user/signup.html', context)

def login_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            current_user =request.user
            # userprofile=UserProfile.objects.get(user_id=current_user.id)
            # request.session['userimage'] = userprofile.image.url
           

            # Redirect to a success page.
            return HttpResponseRedirect('/blog')
        else:
            messages.warning(request,"Login Error !! Username or Password is incorrect")
            return HttpResponseRedirect('/login')
    # Return an 'invalid login' error message.

    # category = Category.objects.all()
    # context = {'category': category
    #  }
    return render(request, 'user/login_form.html')    

def logout_func(request):
    logout(request)
    # if translation.LANGUAGE_SESSION_KEY in request.session:
    #     del request.session[translation.LANGUAGE_SESSION_KEY]
    #     del request.session['currency']
    return HttpResponseRedirect('/blog')    