from django.urls import path
from . import views

urlpatterns = [
    path('/page/profile/user-main-profile-page.html', views.index, name='userProfile')
]