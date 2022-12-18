from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages

from django.contrib.auth import get_user_model
from .models import Profile
User = get_user_model()
# Create your views here.

def index(request):
    return render(request,'index.html')
    
def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password==confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request,"User with this Email already Exists!")
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,"User with this username already Exists!")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                
                #log user in and redirect to settings page
                
                #create a profile object for the new user
                user_model = User.objects.get(username=username)
                user_profile = Profile.objects.create(user=user_model,id_user = user_model.id)
                user_profile.save()
                messages.info(request,f'User Registered with username:{username}')
                return redirect('signup')
        else:
            messages.info(request,"PASSWORD NOT MATCHING")
            return redirect('signup')
        return render(request,'signup.html')
    
        
    return render(request,'signup.html')
    
    