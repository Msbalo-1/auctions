from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib import messages
from .models import Profile
from .form import signupForm
from django.contrib.auth.models import User
# Create your views here.







def signupPage(request):
    form = signupForm
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'successfully created')
            login(request, user)
            return redirect('products')

        else:
            messages.error(request, 'An error occurred')
    context = {'form': form}
    return render(request, 'users/register.html', context)



def loginPage(request):

    if request.user.is_authenticated:
        return redirect('products')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username dose not exit')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'successfully login')
            return redirect('products')
        else:
            messages.error(request, 'Username or password does not exit')

    return render(request, 'users/login.html')


def logoutPage(request):
    logout(request)
    messages.success(request, 'logout successfully')
    return redirect('login')




def profile(request, ):
    # profile = pass
    # context = {'profile': profile}
    return render(request, 'users/user_profile.html', )

