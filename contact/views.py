from django.shortcuts import render,redirect
from .models import Faq,Contact
from django.contrib import messages
# Create your views here.
def faq(request):
    faq = Faq.objects.all()
    context = {
        'faq' : faq,
    }
    return render(request,'contact/faq.html',context)

def contact(request):
  if request.method == 'POST':
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    overview = request.POST['overview']
    subject = request.POST['subject']
    user_id = request.POST['user_id']
    

    #  Check if user has made inquiry already
    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Contact.objects.all().filter( user_id=user_id)
     

    contact = Contact(name=name, email=email, phone=phone,overview=overview, subject=subject, user_id=user_id )

    contact.save()

 

    messages.success(request, 'Your message  has been send')
    return redirect('/contact/contact')

  return render(request,'contact/contact.html')    