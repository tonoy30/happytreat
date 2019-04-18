from .serializers import ProfileSerializer, FoodRequestSerialization, DonatedFoodSerializer
from foodApp.models import FoodRequest, Profile, DonatedFood
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics


class ProfileView(APIView):
    def get(self, format=None):
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=ValueError)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class FoodRequestView(APIView):
    def get(self, format=None):
        food_request = FoodRequest.objects.all()
        serializer = FoodRequestSerialization(food_request, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FoodRequestSerialization(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DonatedFoodView(APIView):
    def get(self, request, format=None):
        donated_food = DonatedFood.objects.all()
        serializer = DonatedFoodSerializer(donated_food, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DonatedFoodSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# class ProfileListView(generics.ListCreateAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer


# class CreateUpdateDestroyProfile(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
