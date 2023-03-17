from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForms

def index(request):
    # order = Order.objects.all()
    context = {}
    return render(request, "auctions/index.html", context)

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
    return render(request, 'auctions/create_product.html', context)

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


