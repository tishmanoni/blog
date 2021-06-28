from django.shortcuts import render
# Create your views here.
from django.shortcuts import render,get_object_or_404

from django.http import HttpResponse
from django.shortcuts import render
# from django.contrib.auth import authenticate, login
# from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm


@login_required
def dashboard(request):
    # messages.success(request, 'Succesfully Logged in')
    current_user = request.user  # Access User Session information
    # profile = Profile.objects.get(user_id=current_user.id)
    # categories = Category.objects.all()
    # cart = Cart(request)
    return render(request,'account/dashboard.html',{'section': 'dashboard'})


def register(request):
    
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
            user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            

            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
        
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})