from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User

def front(request):
        context = { }
        return render(request, "index.html", context)
class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()