from django.urls import path
from . import views
urlpatterns = [
    path('users/', views.account, name='account'),


    # path("login", views.login_view, name="login"),
#     path("logout", views.logout_view, name="logout"),
#     path("register", views.register, name="register")

]
