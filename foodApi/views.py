from .serializers import ProfileSerializer, FoodRequestSerialization
from foodApp.models import FoodRequest, Profile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ProfileView(APIView):
    def get(self, format=None):
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validator_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


class FoodRequestView(APIView):
    def get(self, format=None):
        food_request = FoodRequest.objects.all()
        serializer = FoodRequestSerialization(food_request, many=True)
        return Response(serializer.data)
