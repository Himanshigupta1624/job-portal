from django.shortcuts import render,redirect,get_object_or_404
from job.models import Job,ApplyJob
from django.contrib.auth import logout
from .filter import JobFiter


# def home(request):
#     return render(request,'website/home.html')

def logout_and_redirect_home(request):
    logout(request)
    filter=JobFiter(request.GET,queryset=Job.objects.filter(is_available=True).order_by('-timestamp'))
    context={'filter':filter}
    return render (request,'website/home.html',context)

def job_listing(request):
    jobs=Job.objects.filter(is_available=True).order_by('-timestamp')
    context={'jobs':jobs}
    return render (request,'website/job_listing.html',context)

def job_details(request,pk):
   job = get_object_or_404(Job, pk=pk)
   has_applied = False
   if request.user.is_authenticated:
        has_applied = ApplyJob.objects.filter(user=request.user, job=job).exists()
   context = {'job': job, 'has_applied': has_applied}
   return render(request, 'website/job_details.html', context)




        
