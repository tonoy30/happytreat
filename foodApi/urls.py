from django.urls import path
from . import views

urlpatterns = [
    path('profile-list/', views.ProfileView.as_view(), name='profile-list'),
    path('food-request/', views.FoodRequestView.as_view(), name='food-request'),
    path('donated-food/', views.DonatedFoodView.as_view(), name='donated-food'),
    # TODO: Make avaliable in final realease
    path('profile/', views.ProfileListView.as_view(), name='profiles'),
    path('profile/<int:pk>', views.CreateUpdateDestroyProfile.as_view(), name='create')
]
