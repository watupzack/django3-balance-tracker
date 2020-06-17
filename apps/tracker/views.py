from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import UserBalance


def home(request):
    return render(request, 'tracker/home.html')


@login_required
def userPage(request):
    if request.method == "POST":
        user_balance = UserBalance.objects.get(user=request.user)

        if request.POST.get('updateBalance') == 'putMdl':
            user_balance.mdl += int(request.POST.get('amount'))
        elif request.POST.get('updateBalance') == 'withdrawMdl':
            user_balance.mdl -= int(request.POST.get('amount'))

        elif request.POST.get('updateBalance') == 'putUsd':
            user_balance.usd += int(request.POST.get('amount'))
        elif request.POST.get('updateBalance') == 'withdrawUsd':
            user_balance.usd -= int(request.POST.get('amount'))

        elif request.POST.get('updateBalance') == 'putEur':
            user_balance.eur += int(request.POST.get('amount'))
        elif request.POST.get('updateBalance') == 'withdrawEur':
            user_balance.eur -= int(request.POST.get('amount'))

        elif request.POST.get('updateBalance') == 'putRon':
            user_balance.ron += int(request.POST.get('amount'))
        elif request.POST.get('updateBalance') == 'withdrawRon':
            user_balance.ron -= int(request.POST.get('amount'))
        # if request.POST.get('updateBalance') == 'put':
        #     if request.POST.get('name') == "ronForm":
        #         user_balance.ron += int(request.POST.get('amount'))
        #     elif request.POST.get('name') == "usdForm":
        #         user_balance.usd += request.POST.get('amount')
        #     elif request.POST.get('name') == "eurForm":
        #         user_balance.eur += request.POST.get('amount')
        #     elif request.POST.get('name') == "mdlForm":
        #         user_balance.mdl += request.POST.get('amount')
        #
        # elif request.POST.get('updateBalance') == 'withdraw':
        #     if request.POST.get('name') == "ronForm":
        #         user_balance.ron -= int(request.POST.get('amount'))
        #     elif request.POST.get('name') == "usdForm":
        #         user_balance.usd -= request.POST.get('amount')
        #     elif request.POST.get('name') == "eurForm":
        #         user_balance.eur -= request.POST.get('amount')
        #     elif request.POST.get('name') == "mdlForm":
        #         user_balance.mdl -= request.POST.get('amount')


        user_balance.save()
        return redirect('userPage')
    else:
        user_balance = UserBalance.objects.get(user=request.user)
        context = {'user_balance': user_balance}
        return render(request, 'tracker/userpage.html', context)


def signUpUser(request):
    if request.method == "POST":
        if request.POST.get('password1') == request.POST.get('password2'):
            try:
                user = User.objects.create_user(username=request.POST.get('username'),
                                                password=request.POST.get('password1'),
                                                first_name=request.POST.get('first_name'),
                                                last_name=request.POST.get('last_name'))
                user.save()
                user_balance = UserBalance.objects.create(user=user, mdl=0, eur=0, usd=0)
                user_balance.save()
                login(request, user)
                return redirect('userPage')
            except IntegrityError:
                return render(request, 'tracker/signup.html', {'error':'That username has been already taken'})
        else:
            return render(request, 'tracker/signup.html', {'error':'Passwords do not match'})
    else:
        return render(request, 'tracker/signup.html')


@login_required
def logOutUser(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')


def logInUser(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST.get('username'),
                                     password=request.POST.get('password'))
        if user is None:
            return render(request, 'tracker/login.html', {'error':'Username and password do not match'})
        else:
            login(request, user)
            return redirect('userPage')
    else:
        return render(request, 'tracker/login.html')
