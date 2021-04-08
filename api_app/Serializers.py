from rest_framework import serializers
from api_app.models import UserProfile
from api_app.models import UserMoment

class UserProfileSerializer(serializers.ModelSerializer):
    """serializer the user"""
    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'name', 'phone', 'password')
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        """create and return a new user"""
        user = UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password'],
            phone = validated_data['phone'],
        )

        return user


class UserMomentSerializer(serializers.ModelSerializer):
    """we will serialize the details of the moment posted by the user"""
    class Meta:
        model = UserMoment
        fields = ('user_profile', 'momentTitle', 'momentText', 'created_on')
        extra_kwargs = {'created_on': {'read_only':True}}
