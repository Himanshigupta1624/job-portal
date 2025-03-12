from django.shortcuts import render,redirect

def dashbaord(request):
    return render(request,'dashboard/dashboard.html')