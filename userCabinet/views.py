from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'userCabinet/page/profile/user-main-profile-page.html')
