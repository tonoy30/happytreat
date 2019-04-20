from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', views.home, name='home'),
    path('login', loginView, {
         'template_name': 'login.html'}, name='login'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('signup/', views.signup, name='signup'),
    path('forget_password/', views.forget_password, name='forget_password'),
    path('about_us/', views.about_us, name='about_us')
]
