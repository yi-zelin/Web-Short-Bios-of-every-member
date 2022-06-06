from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def mainpage(request):
   return render(request, "mainpage.html")

def user_list(request):
    return render(request, "user_list.html")