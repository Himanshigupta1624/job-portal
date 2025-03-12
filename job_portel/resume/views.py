from django.shortcuts import render,redirect
from .models import REsume
from .forms import UpdateResumeForm
from django.contrib import messages
from users.models import CustomUser


def update_resume(request):
    if not request.user.is_authenticated:
        messages.warning(request, "You need to be logged in to update your resume.")
        return redirect('login')

    resume, created = REsume.objects.get_or_create(user=request.user)
    if request.method=='POST':
        form=UpdateResumeForm(request.POST,request.FILES,instance=resume)
        if form.is_valid():
            var=form.save(commit=False)
            request.user.has_resume=True
            request.user.save()
            var.save()
            messages.info(request,"Your resume has been created successfully.")
            return redirect("dashboard")
        else:
            messages.warning(request,"Something went wrong")
    else:
        form=UpdateResumeForm(instance=resume)
        context={'form':form,'is_created':created}
        return render(request,'resume/update_resume.html',context)        
    
# def resume_details(request,pk):
#     resume=REsume.objects.get(pk=pk)
#     context={'resume':resume}
#     return render(request,'resume/resume_details.html',context)    
def modify_resume(request):
    try:
        resume = REsume.objects.get(user=request.user)
    except REsume.DoesNotExist:
        messages.warning(request, "You need to create a resume first.")
        return redirect('update-resume')
        
    if request.method == 'POST':
        form = UpdateResumeForm(request.POST, request.FILES, instance=resume)
        if form.is_valid():
            form.save()
            messages.success(request, "Your resume has been updated successfully.")
            return redirect("dashboard")
        else:
            messages.warning(request, "Your company information has been updated. ")
    else:
        form = UpdateResumeForm(instance=resume)
    
    context = {'form': form}
    return render(request, 'resume/modify_resume.html', context)
    

