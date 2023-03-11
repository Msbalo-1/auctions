from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Profile, Product





# def login_view(request):
#     if request.method == "POST":
#
#         # Attempt to sign user in
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username=username, password=password)
#
#         # Check if authentication successful
#         if user is not None:
#             login(request, user)
#             return redirect(reverse("index"))
#         else:
#             messages.error("Invalid username and/or password.")
#             return render(request, "auctions/login.html")
#
#     else:
#         return render(request, "auctions/login.html")
#
#
# def logout_view(request):
#     logout(request)
#     return redirect('auctions')
#
#
# def register(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         email = request.POST["email"]
#
#         # Ensure password matches confirmation
#         password = request.POST["password"]
#         confirmation = request.POST["confirmation"]
#         if password != confirmation:
#             messages.error("Passwords must match.")
#             return render(request, "auctions/register.html")
#
#         # Attempt to create new user
#         try:
#             user = Profile.objects.create_user(username, email, password)
#             user.save()
#         except IntegrityError:
#             return render(request, "auctions/register.html", {
#                 "message": "Username already taken."
#             })
#         login(request, user)
#         return redirect(reverse("index"))
#     else:
#         return render(request, "auctions/register.html")


def index(request):
    return render(request, "auctions/index.html")


def auctions(request):
    product = Product.objects.all()
    context = {'product': product}
    return render(request, 'auctions/all-auctions.html', context)


def auction(request, pk):
    productobj = Product.objects.get(id=pk)
    context = {'product': productobj}
    return render(request, 'auction/auction-detail.html', context)








