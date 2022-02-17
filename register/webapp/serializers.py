from rest_framework import serializers
from django.contrib.auth.models import User, UserManager
from .models import Userdata

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userdata
        fields = ('first_name', 'last_name','date_of_birth', 'username', 'address', 'email_id', 'phone',
                  'password', 'confirm_password')



