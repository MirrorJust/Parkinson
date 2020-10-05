from django.shortcuts import render
from django.http import HttpResponse

#Основная страница landing----------------------------------------------------------------------


def index(request):
    return render(request, 'landingPage/index.html')

#Личный кабинет профиль-------------------------------------------------------------------------


def profile(request):
    return render(request, 'landingPage/page/profile/user-main-profile-page.html')

#Личный кабинет База знаний---------------------------------------------------------------------


def symptomsAtt(request):
    return render(request, 'landingPage/page/symptoms/know-base-attention-page.html')


def symptomsTreat(request):
    return render(request, 'landingPage/page/symptoms/know-base-treatment-page.html')


def symptomsCompl(request):
    return render(request, 'landingPage/page/symptoms/know-base-complications-page.html')


def symptomsSympt(request):
    return render(request, 'landingPage/page/symptoms/know-base-symptoms-page.html')


#Личный кабинет Обучение-----------------------------------------------------------------------


def trainingBal(request):
    return render(request, 'landingPage/page/training/training-balance-exercises.html')


def trainingRul(request):
    return render(request, 'landingPage/page/training/training-execution-rules.html')


def trainingFreezWalk(request):
    return render(request, 'landingPage/page/training/training-freezing-walk.html')


def trainingGeneral(request):
    return render(request, 'landingPage/page/training/training-general-exercises.html')


def trainingPrivate(request):
    return render(request, 'landingPage/page/training/training-private-exercises.html')

#Личный кабинет Тренировка памяти


def memoryMain(request):
    return render(request, 'landingPage/page/memory/memory-main.html')

#Личный кабинет Обратная связь

def feedback(request):
    return render(request, 'landingPage/page/feedback/feedback-main.html')

