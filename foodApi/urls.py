from django.urls import path, include
from . import views

urlpatterns = [
    # Authentication url
    path('rest-auth/', include('rest_auth.urls')),
    # Serving url
    path('profile-list/', views.ProfileView.as_view(), name='profile-list'),
    path('food-request/', views.FoodRequestView.as_view(), name='food-request'),
    path('donated-food/', views.DonatedFoodView.as_view(), name='donated-food'),
    # TODO: Make avaliable in final realease
    path('profile/', views.ProfileListView.as_view(), name='profiles'),
    path('profile/<int:pk>', views.CreateUpdateDestroyProfile.as_view(), name='create')
]
