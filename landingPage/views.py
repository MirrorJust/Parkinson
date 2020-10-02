from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'landingPage/index.html')

def profile(request):
    return render(request, 'landingPage/page/profile/user-main-profile-page.html')

def symptomsAtt(request):
    return render(request, 'landingPage/page/symptoms/know-base-attention-page.html')

def symptomsTreat(request):
    return render(request, 'landingPage/page/symptoms/know-base-treatment-page.html')

def symptomsCompl(request):
    return render(request, 'landingPage/page/symptoms/know-base-complications-page.html')

def symptomsSympt(request):
    return render(request, 'landingPage/page/symptoms/know-base-symptoms-page.html')
