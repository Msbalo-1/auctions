from django.urls import path
from . import views

urlpatterns = [

    path('account/', views.profile, name='profile'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('signup/', views.signupPage, name='signup'),

]
