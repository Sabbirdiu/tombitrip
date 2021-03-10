from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from django.http import HttpResponse
import datetime
from .models import Post,Category,Comment,CommentForm
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
def blogdetails(request,slug):
    # get post object
    post = get_object_or_404(Post,  slug=slug)
    # news_featured = Post.objects.filter(featured=True).order_by('-timestamp')[0:4]
    posts = Post.objects.all()
   
    # list of active parent comments
    comments = post.comments.filter(active=True, parent__isnull=True)
    if request.method == 'POST':
        # comment has been added
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            parent_obj = None
            # get parent comment id from hidden input
            try:
                # id integer e.g. 15
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            # if parent_id has been submitted get parent_obj id
            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)
                # if parent object exist
                if parent_obj:
                    # create replay comment object
                    replay_comment = comment_form.save(commit=False)
                    # assign parent_obj to replay comment
                    replay_comment.parent = parent_obj
            # normal comment
            # create comment object but do not save to database
            new_comment = comment_form.save(commit=False)
            # assign ship to the comment
            new_comment.post = post
            # save
            new_comment.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form = CommentForm()
    return render(request,'blog/blogdetails.html',
                  {'obj': post,
                  
                   'comments': comments,
                   'posts':posts,
                  
                   'comment_form': comment_form})    