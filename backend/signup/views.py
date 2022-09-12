from django.shortcuts import render
from rest_framework import viewsets
from .serializers import NewUserSerializer
from .models import NewUser


class NewUserView(viewsets.ModelViewSet):
    serializer_class = NewUserSerializer
    queryset = NewUser.objects.all()
