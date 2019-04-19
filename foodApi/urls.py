from django.urls import path, include
from . import views

urlpatterns = [
    # Authentication url
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    # Serving url
    path('profile-list/', views.ProfileListView.as_view(), name='profile-list'),
    path('profile-list/', views.RetrieveUpdateDestroyProfileListView.as_view(),
         name='edit-profile-list'),
    path('food-request/', views.FoodRequestListView.as_view(), name='food-request'),
    path('food-request/<int:pk>/',
         views.CreateUpdateDestroyFoodRequest.as_view(), name='edit-food-request'),
    path('donated-food/', views.DonatedFoodListView.as_view(), name='donated-food'),
    path('donated-food/<int:pk>/',
         views.CreateUpdateDestroyDonatedFood.as_view(), name='edit-donated-food'),
]
