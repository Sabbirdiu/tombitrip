from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Post,Category,Comment
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.
def blog(request):
    blog = Post.objects.order_by('-timestamp')
    categories = Category.objects.filter()
    paginator = Paginator(blog, 2)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    # category_count = get_category_count()

    context = {
        'listings':paged_listings,
        'categories':categories,
        
    }
    return render(request, 'blog/blog.html',context)