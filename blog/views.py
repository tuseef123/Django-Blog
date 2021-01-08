from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import post
# Create your views here.

def home(request):
    posts = post.objects.all()
    return render(request, 'blog/home.html',{'posts':posts})
def about(request):
    return render(request,'blog/about.html',{'title':'About'})
