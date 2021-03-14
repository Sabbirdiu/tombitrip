from django.shortcuts import render
from .models import Faq
# Create your views here.
def faq(request):
    faq = Faq.objects.all()
    context = {
        'faq' : faq,
    }
    return render(request,'contact/faq.html',context)