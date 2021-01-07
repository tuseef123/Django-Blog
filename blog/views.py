from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    post = [
        {
            'title':'Blog Post 1',
            'author':'Tauseef',
            'content':'This is the very first post',
            'date_posted':'Jan,6 2021'
        },
        {
            'title':'Blog Post 2',
            'author':'admin',
            'content':'This is the very second post',
            'date_posted':'Jan,6 2021'
        },
    ]
    return render(request, 'blog/home.html',{'posts':post})
def about(request):
    return render(request,'blog/about.html',{'title':'About'})
