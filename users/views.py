from django.shortcuts import render,redirect
from .forms import UserRegistrationForm,UserUpdateForm,ProfileUpdateForm
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
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        u_profile = ProfileUpdateForm(request.POST ,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and u_profile.is_valid():
            u_form.save()
            u_profile.save()
            messages.success(request,f'Profile Updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        u_profile = ProfileUpdateForm(instance=request.user.profile)
    return render(request,'users/profile.html',{'u_form':u_form,'u_profile':u_profile})

def check(request):
    return render(request,'users/check.html')