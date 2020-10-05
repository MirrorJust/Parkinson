from django.urls import path
from . import views

urlpatterns = [
    #Основная страница landing
    path('', views.index, name='mainPage'),

    #Личный кабинет профиль
    path('page/profile/user-main-profile-page', views.profile, name='profilePage'),

    #Личный кабинет База знаний
    path('page/symptoms/know-base-symptoms-page', views.symptomsSympt, name='symptomsSymptoms'),
    path('page/symptoms/know-base-treatment-page', views.symptomsTreat, name='symptomsTreatment'),
    path('page/symptoms/know-base-complications-page', views.symptomsCompl, name='symptomsComplications'),
    path('page/symptoms/know-base-attention-page', views.symptomsAtt, name='symptomsAttention'),

    #Личный кабинет Обучение
    path('page/training/training-balance-exercises', views.trainingBal, name='trainingBalance'),
    path('page/training/training-execution-rules', views.trainingRul, name='trainingRules'),
    path('page/training/training-freezing-walk', views.trainingFreezWalk, name='trainingFreezingWalk'),
    path('page/training/training-general-exercises', views.trainingGeneral, name='trainingGeneral'),
    path('page/training/training-private-exercises', views.trainingPrivate, name='trainingPrivate'),

    #Личный кабинет Тренировка памяти
    path('page/memory/memory-main', views.memoryMain, name='memoryMain'),

    #Личный кабинет Обратная связь
    path('page/feedback/feedback-main', views.feedback, name='feedback'),
]
