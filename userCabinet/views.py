from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


#Личный кабинет профиль-------------------------------------------------------------------------


def profile(request):
    return render(request, 'userCabinet/page/profile/user-main-profile-page.html')

#Личный кабинет База знаний---------------------------------------------------------------------


def symptomsAtt(request):
    return render(request, 'userCabinet/page/symptoms/know-base-attention-page.html')


def symptomsTreat(request):
    return render(request, 'userCabinet/page/symptoms/know-base-treatment-page.html')


def symptomsCompl(request):
    return render(request, 'userCabinet/page/symptoms/know-base-complications-page.html')


def symptomsSympt(request):
    return render(request, 'userCabinet/page/symptoms/know-base-symptoms-page.html')


#Личный кабинет Обучение-----------------------------------------------------------------------


def trainingBal(request):
    return render(request, 'userCabinet/page/training/training-balance-exercises.html')


def trainingRul(request):
    return render(request, 'userCabinet/page/training/training-execution-rules.html')


def trainingFreezWalk(request):
    return render(request, 'userCabinet/page/training/training-freezing-walk.html')


def trainingGeneral(request):
    return render(request, 'userCabinet/page/training/training-general-exercises.html')


def trainingPrivate(request):
    return render(request, 'userCabinet/page/training/training-private-exercises.html')

#Личный кабинет Тренировка памяти


def memoryMain(request):
    return render(request, 'userCabinet/page/memory/memory-main.html')

#Личный кабинет Обратная связь

def feedback(request):
    return render(request, 'userCabinet/page/feedback/feedback-main.html')

