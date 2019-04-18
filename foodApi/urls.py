from django.urls import path
from . import views

urlpatterns = [
    path('profile-list/', views.ProfileView.as_view(), name='profile-list'),
    path('food-request/', views.FoodRequestView.as_view(), name='food-request')
]
