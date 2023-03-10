from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Profile, Product
from .forms import ProductForms




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
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'auctions/products.html', context)


def auction(request, pk):
    productobj = Product.objects.get(id=pk)
    context = {'product': productobj}
    return render(request, 'auctions/single_product.html', context)


def createProduct(request):
    form = ProductForms()
    if request.method == 'POST':
        form = ProductForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')


    context = {'form': form}
    return render(request, 'auctions/product_forms.html', context)

def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForms(instance=product)
    if request.method == 'POST':
        form = ProductForms(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')


    context = {'form': form}

    return render(request, 'auctions/product_forms.html', context)

def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)

    if request.method == "POST":
        product.delete()
        return redirect('products')

    context = {'item': product}
    return render(request, 'auctions/delete_forms.html', context)


