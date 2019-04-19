from .serializers import ProfileSerializer, FoodRequestSerialization, DonatedFoodSerializer
from foodApp.models import FoodRequest, Profile, DonatedFood
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics


class ProfileListView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class RetrieveUpdateDestroyProfileListView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class FoodRequestListView(generics.ListCreateAPIView):
    queryset = FoodRequest.objects.all()
    serializer_class = FoodRequestSerialization


class CreateUpdateDestroyFoodRequest(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoodRequest.objects.all()
    serializer_class = FoodRequestSerialization


class DonatedFoodListView(generics.ListCreateAPIView):
    queryset = DonatedFood.objects.all()
    serializer_class = DonatedFoodSerializer


class CreateUpdateDestroyDonatedFood(generics.RetrieveUpdateDestroyAPIView):
    queryset = DonatedFood.objects.all()
    serializer_class = DonatedFoodSerializer
