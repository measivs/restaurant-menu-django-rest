from django.contrib.auth.models import User
from rest_framework import serializers

from users.models import CustomUser


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(max_length=20, required=False, allow_blank=True)
    profile_picture = serializers.ImageField(required=False, allow_null=True)
    address = serializers.CharField(max_length=255, required=False, allow_blank=True)
    is_restaurant_owner = serializers.BooleanField(required=False, default=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'phone_number', 'profile_picture', 'address', 'is_restaurant_owner']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            phone_number=validated_data.get('phone_number', ''),
            profile_picture=validated_data.get('profile_picture', None),
            address=validated_data.get('address', ''),
            is_restaurant_owner=validated_data.get('is_restaurant_owner', False)
        )
        return user