from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForms

def index(request):
    profile = request.user.profile
    products = Product.objects.all()
    my_products = profile.product_set.all()

    context = {'products': products, 'my_products': my_products}
    return render(request, "auctions/index.html", context)

def auctions(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'auctions/products.html', context)



@login_required(login_url='login')
def auction(request, pk):
    productobj = Product.objects.get(id=pk)
    context = {'product': productobj}
    return render(request, 'auctions/single_product.html', context)



@login_required(login_url='login')
def createProduct(request):
    profile = request.user.profile
    form = ProductForms()
    if request.method == 'POST':
        form = ProductForms(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = profile
            product.save()
            return redirect('profile')

    context = {'form': form}
    return render(request, 'auctions/create_product.html', context)


@login_required(login_url='login')
def updateProduct(request, pk):
    profile = request.user.profile
    product = profile.product_set.get(id=pk)
    form = ProductForms(instance=product)
    if request.method == 'POST':
        form = ProductForms(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('profile')


    context = {'form': form}

    return render(request, 'auctions/product_forms.html', context)



@login_required(login_url='login')
def deleteProduct(request, pk):
    profile = request.user.profile
    product = profile.product_set.get(id=pk)
    if request.method == "POST":
        product.delete()
        return redirect('profile')

    context = {'item': product}
    return render(request, 'auctions/delete_forms.html', context)



def dashboard(requst):
    context = {}
    return render(requst, 'auctions/dashboard.html', context)

