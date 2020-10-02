from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='mainPage'),
    path('page/profile/user-main-profile-page', views.profile, name='profilePage'),
    path('page/symptoms/know-base-symptoms-page', views.symptomsSympt, name='symptomsSymptoms'),
    path('page/symptoms/know-base-treatment-page', views.symptomsTreat, name='symptomsTreatment'),
    path('page/symptoms/know-base-complications-page', views.symptomsCompl, name='symptomsComplications'),
    path('page/symptoms/know-base-attention-page', views.symptomsAtt, name='symptomsAttention'),
]
