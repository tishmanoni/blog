from django.shortcuts import render
# Create your views here.
from django.shortcuts import render,get_object_or_404

from django.http import HttpResponse
from django.shortcuts import render
# from django.contrib.auth import authenticate, login
# from .forms import LoginForm
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    # messages.success(request, 'Succesfully Logged in')
    current_user = request.user  # Access User Session information
    # profile = Profile.objects.get(user_id=current_user.id)
    # categories = Category.objects.all()
    # cart = Cart(request)
    return render(request,'account/dashboard.html',{'section': 'dashboard'})

