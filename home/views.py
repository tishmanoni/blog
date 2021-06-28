from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from home.forms import SearchForm
from django.db.models import Avg, Count, Q, F
from blog.models import Post
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import PostForm
from .models import Mypost

# def simple_upload(request):
  
#     return render(request, 'home/index.html')

# Create your views here.


def home(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'home/index.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, "home/index.html", {})


# def home(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             data = Mypost()  # create relation with model
#             data.title = form.cleaned_data['title']
#             data.image = form.cleaned_data['image']
#             current_user = request.user
#             data.author_id = current_user.id
#             data.detail = form.cleaned_data['detail']
#             data.files = form.cleaned_data['files']
           
#             data.save() 
#             form.save()
#             return redirect('/')
#     else:
#         form = PostForm()
#     return render(request, "home/index.html", {
#         'form': form
#     })


def search(request):
    if request.method == 'POST': # check post
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query'] # get form input data
            posts = Post.objects.filter(title__icontains=query)

            
            context = {'posts': posts, 'query':query,
                        }
            return render(request, 'home/search.html', context)

    return HttpResponseRedirect('/')


