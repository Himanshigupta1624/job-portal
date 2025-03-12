from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from users.models import CustomUser
from .models import Job,ApplyJob
from .forms import CreateJobForm,UpdateJobForm
from comapny.models import Comapny

def create_job(request):
    if not request.user.is_authenticated:
        messages.warning(request, "You need to be logged in to create a job.")
        return redirect('login')

    if not request.user.has_company:
        messages.warning(request, "You need to create a company before creating a job.")
        return redirect('update-company')
    try:
        company = request.user.company
    except Comapny.DoesNotExist:
        messages.warning(request, "You need to create a company before creating a job.")
        return redirect('update-company')
    
    if request.method=='POST':
        form=CreateJobForm(request.POST)
        if form.is_valid():
            var=form.save(commit=False)
            var.user=request.user
            var.company=company
            var.save()
            messages.info(request,"New Job has been created.")
            return redirect('dashboard')
        else:
            messages.warning(request,"Something went wrong.")
            return redirect('create-job')
    else:
        form=CreateJobForm()
    context={'form':form}
    return render(request,'job/create_job.html',context)        



def update_job(request,pk):
    # if not request.user.is_authenticated:
    #     messages.warning(request, "You need to be logged in to create a job.")
    #     return redirect('login')

    # if not request.user.has_company:
    #     messages.warning(request, "You need to create a company before creating a job.")
    #     return redirect('update-company')
    job=get_object_or_404(Job, pk=pk)
    if request.method =='POST':
        form=UpdateJobForm(request.POST,instance=job)
        if form.is_valid():
            form.save()
            messages.info(request,"Your Job info is updated.")
            return redirect('dashboard')
        else:
            messages.warning(request,"Something went wrong.")
    else:
        form=UpdateJobForm(instance=job)
        context={'form':form}
        return render(request,'job/update_job.html',context) 
           


def manage_jobs(request):
    if not request.user.is_authenticated:
        messages.warning(request, "You need to be logged in to manage jobs.")
        return redirect('login')

    try:
        company = request.user.company
    except Comapny.DoesNotExist:
        messages.warning(request, "You need to create a company before managing jobs.")
        return redirect('update-company')
    jobs=Job.objects.filter(user=request.user,company=request.user.company)
    context={'jobs':jobs}
    return render (request,'job/manage_jobs.html',context)


def apply_to_job(request,pk):
    if request.user.is_authenticated:
        job=Job.objects.get(pk=pk)
        if ApplyJob.objects.filter(user=request.user,job=pk).exists():
            messages.warning(request,"Permission Denied")
            return redirect('dashboard')
        else:
            ApplyJob.objects.create(
                job=job,
                user=request.user,
                status='Pending'
            )
            messages.info(request,"You have sucessfully applied! Please see Dashboard.")
            return redirect('dashboard')
    else:
        messages.info(request,"Please log in to continue.")
        return redirect('login')
    
def all_applicants(request,pk):
    job=Job.objects.get(pk=pk)
    applicants=job.applications.all()
    context={'job':job,'applicants':applicants}
    return render(request,'job/all_applicants.html',context)

def applied_job(request):
    jobs=ApplyJob.objects.filter(user=request.user) 
    context={'jobs':jobs} 
    return render(request,'job/applied_job.html',context)  