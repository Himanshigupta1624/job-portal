from django.shortcuts import render,redirect
from django.contrib import messages
from . models import Comapny
from . forms import UpdateCompanyForm
from users.models import CustomUser,AbstractBaseUser

# update company 
def update_company(request):
    if not request.user.is_authenticated:
        messages.warning(request, "You need to be logged in to update company information.")
        return redirect('login')

    if not request.user.is_recruiter:
        messages.warning(request, "Permission denied.")
        return redirect('dashboard') 
    
    try:
        company = Comapny.objects.get(user=request.user)
    except Comapny.DoesNotExist:
        company = None
    if request.method=='POST':
        form=UpdateCompanyForm(request.POST,instance=company)
        if form.is_valid():
            var=form.save(commit=False)
            user=CustomUser.objects.get(id=request.user.id)
            user.has_company=True
            var.save()
            user.save()
            messages.info(request,'Your company information has been updated.  ')
            return redirect('dashboard')
        else:
            messages.warning(request,"Something went wrong")
    else:
        form=UpdateCompanyForm(instance=company)
        context={'form':form}
        return render(request,'comapny/update_company.html',context)
   

def modify_company(request):
    try:
        company=Comapny.objects.get(user=request.user)
    except Comapny.DoesNotExist:
        messages.warning(request, "You need to create a Company first.")
        return redirect('update-company')
    if request.method=='POST':
        form=UpdateCompanyForm(request.POST,request.FILES,instance=company)
        if form.is_valid():
            form.save()
            messages.success(request,"Your company information has been updated.")
            return redirect("dashboard")
        else:
            messages.warning(request,"Please correct the error below.")
    else:
        form=UpdateCompanyForm(instance=company)
    context={'form':form}
    return render(request,"comapny/modify_company.html",context)           
        
       