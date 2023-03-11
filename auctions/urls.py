from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("products/", views.auctions, name="products"),
    path("product/<str:pk>/", views.auction, name="product"),



    # path("login", views.login_view, name="login"),
#     path("logout", views.logout_view, name="logout"),
#     path("register", views.register, name="register")
]
