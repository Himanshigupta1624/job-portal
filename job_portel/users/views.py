from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import CustomUser
from .forms import RegisterUserForm
from resume.models import REsume
from comapny.models import Comapny



def register_applicant(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_applicant = True
            user.is_recruiter = False
              # Assuming you have an is_applicant field in your user model
            user.username = user.email
            user.save()
            messages.success(request, 'Your account has been created. Please login.')
            return redirect('login')
        else:
            messages.warning(request, 'Something went wrong. Please check the form for errors.')
    else:
        form = RegisterUserForm()
    
    context = {'form': form}
    return render(request, 'users/register_applicant.html', context)

# recruiters only  
def register_recruiter(request):
    if request.method=='POST':
        form=RegisterUserForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_recruiter = True
            user.is_applicant = False 
            
            user.username=user.email
            user.save()
            Comapny.objects.create(user=user)
            messages.info(request,'Your account has been created. Please login ')
            return redirect('login')
        else:
            messages.warning(request,'Something went wrong')
            return redirect('register-recruiter')
    else:
        form=RegisterUserForm()
        context={'form':form}    
        return render(request,'users/register_recruiter.html',context)
# login user

def login_user(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        
        user=authenticate(request, username=email,password=password)
        if user is not None and user.is_active:
            login(request,user) 
            if user.is_recruiter:
                return redirect('dashboard')
            elif user.is_applicant:
                return redirect('dashboard') 
        else:
            messages.warning(request,"Something went wrong.")
            return redirect('login')
    else:
        return render(request,'users/login.html')         
#logout user
def logout_user(request):
    logout(request)
    messages.info(request,'Your session has been ended,Please try again later.')
    return redirect('login')
         