from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method =='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account has been created you can now login!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request,'users/register.html',{'form':form})
@login_required
def profile(request):
    return render(request,'users/profile.html')

def check(request):
    return render(request,'users/check.html')