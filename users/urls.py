from django.urls import path
from . import views

urlpatterns = [

    path('account/', views.userAccount, name='profile'),
    path('edit_account/', views.editAccount, name='edit_account'),

    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('signup/', views.signupPage, name='signup'),

]
