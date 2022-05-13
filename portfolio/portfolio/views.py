from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return render(request,'index.html')


def portfolio_class(request):
    return render(request,'portfolio_class.html')

def portfolio_job(request):
    return render(request,'portfolio_job.html')
    