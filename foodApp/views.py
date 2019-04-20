from django.shortcuts import render
from django.http import HttpResponse
from .models import FoodRequest, Profile
# Create your views here.


def home(request):
    return render(request, 'home.html', {})


def login_view(request):
    return render(request, 'login.html', {})


def signup(request):
    return render(request, 'register.html', {})


def forget_password(request):
    return render(request, 'forgot-password.html', {})


def about_us(request):
    return render(request, 'about_us.html', {})


def leaderboard(request):
    donator_list = []
    donator_name = []
    data = FoodRequest.objects.order_by('quantity').values(
        'quantity').values('donator__user')
    for m in data:
        for k, v in m.items():
            print(k, v)
            donator_list.append(v)
    for i in range(len(donator_list)):
        donator = Profile.objects.filter(user_id=donator_list[i]).values()
        for m in donator:
            for k, v in m.items():
                print(k, v)
                donator_name.append(v)
    return render(request, 'leaderboard.html', {'donator_list': donator_list})
