from rest_framework import serializers
from loginapi.models import Loginapi


class LoginapiSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=True, allow_blank=False, max_length=100)
    password = serializers.CharField(required=True, allow_blank=False, max_length=100)

    def create(self, validated_data):
        return Loginapi.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance