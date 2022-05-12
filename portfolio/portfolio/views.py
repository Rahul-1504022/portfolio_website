from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return render(request,'index.html')


def portfolio(request):
    return render(request,'portfolio.html')
    