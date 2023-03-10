from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),

    path("create_product/", views.createProduct, name="add_product"),
    path("update_product/<str:pk>/", views.updateProduct, name="edit_product"),
    path("delete_product/<str:pk>/", views.deleteProduct, name="delete_product"),



    path("products/", views.auctions, name="products"),
    path("product/<str:pk>/", views.auction, name="product"),



    # path("login", views.login_view, name="login"),
#     path("logout", views.logout_view, name="logout"),
#     path("register", views.register, name="register")
]
