from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html',{'name':'Ritik'})

def add(request):
    res = int(request.GET['n1'])+int(request.GET['n2'])
    return render(request, 'result.html',{'res':res})