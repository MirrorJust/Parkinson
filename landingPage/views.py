from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserOurRegistration

#Основная страница landing----------------------------------------------------------------------


def index(request):
    return render(request, 'landingPage/index.html')


def userReg(request):
    if request.method == 'POST':
        form = UserOurRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('profilePage')
    else:
        form = UserOurRegistration()
    return render(request, 'landingPage/user_log/registration.html', {'form': form})
