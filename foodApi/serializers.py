from rest_framework import serializers, status

from foodApp.models import Profile, FoodRequest, DonatedFood

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Profile
        fields = ('user', 'address', 'phone_number',
                  'volunter', 'avaliable')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(
            UserSerializer(), validated_data=user_data)
        profile, createed = Profile.objects.update_or_create(user=user,
                                                             address=validated_data.pop(
                                                                 'address'),
                                                             phone_number=validated_data.pop(
                                                                 'phone_number'),
                                                             volunter=validated_data.pop(
                                                                 'volunter'),
                                                             avaliable=validated_data.pop('avaliable'))
        return profile


class FoodRequestSerialization(serializers.ModelSerializer):
    class Meta:
        model = FoodRequest
        fields = ('donator', 'location', 'quantity', 'expire_time',
                  'food_desc', 'pick_up_time', 'food_status')


class DonatedFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonatedFood
        fields = ('volunter', 'donated_area',
                  'beneficent', 'donated_by', 'finished')
