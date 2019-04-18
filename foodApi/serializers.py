from rest_framework import serializers, status

from foodApp.models import Profile, FoodRequest

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

    def create(self, validator_data):
        user_data = validator_data.pop('user')
        user = UserSerializer.create(
            UserSerializer(), validator_data=user_data)
        profile, createed = Profile.objects.update_or_create(user=user,
                                                             address=validator_data.pop(
                                                                 'address'),
                                                             phone_number=validator_data.pop(
                                                                 'phone_number'),
                                                             volunter=validator_data.pop(
                                                                 'volunter'),
                                                             avaliable=validator_data.pop('avaliable'))


class FoodRequestSerialization(serializers.ModelSerializer):
    class Meta:
        model = FoodRequest
        fields = ('food_id', 'donator', 'location', 'quantity', 'expire_time',
                  'food_desc', 'pick_up_time', 'food_status')
