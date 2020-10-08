from django.urls import path, include
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    #Основная страница landing
    path('', views.index, name='mainPage'),
    path('page/', include('userCabinet.urls')),
    path('registration/', views.userReg, name='userRegistration'),
    path('login/', authViews.LoginView.as_view(template_name='landingPage/user_log/login.html'), name='userLog')
]




