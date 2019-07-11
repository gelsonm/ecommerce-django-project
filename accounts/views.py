from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from django.urls import reverse
from .forms import UserLoginForm, UserRegistrationForm
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))


def user_login(request):
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        #if user_form.is_valid():
        user =authenticate(username=request.POST.get('username'),
                                password=request.POST.get('password'))
        print(user)
        if user:
                login(request, user)
                messages.success(request, "You have successfully logged in")
                
                if request.GET and request.GET['next'] !='':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect('index')
        else:
            messages.error(request, "Log in Unsuccessful!")
    else:
        user_form = UserLoginForm()
        print('user not found')

    args = {'user_form': user_form, 'next': request.GET.get('next', '')}
    return render(request, 'login.html', args)

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password1'))
            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                
                if request.GET and request.GET['next'] !='':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect('index')
            else:
                messages.error(request, "Log in Unsuccessful!")
    else:
        user_form = UserRegistrationForm()

    args = {'user_form': user_form}
    return render(request, 'register.html', args)

''' 
@login_required'''
def profile(request):
    return render(request, 'profile.html')
