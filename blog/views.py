
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post 
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage,\
                                  PageNotAnInteger

# Create your views here.

# def home(request):
#     return HttpResponse("Hello")


def postlist(request):
    object_list = Post.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(object_list, 2) # 2 posts in each page
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        post = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        post = paginator.page(paginator.num_pages)
    return render(request, "blog/list.html", {"post":post, "page":page})


def postdetail(request, year, month, day, slug):
    post = get_object_or_404( Post, slug=slug, status='published', publish__year= year, publish__month= month, publish__day = day)
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, "blog/detail.html", {"post":post, "comments":comments, "new_comment":new_comment, "comment_form":comment_form})
    
    

