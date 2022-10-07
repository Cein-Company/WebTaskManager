from rest_framework import serializers
from signup.models import NewUser


class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ('id', 'name', 'email', 'username', 'password', 'passrepeat')
