"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from todo import views
from rest_framework import routers
from signup import views as signup_views
from login import views as login_views

router = routers.DefaultRouter()
router.register(r'tasks', views.TodoView, 'task')

router1 = routers.DefaultRouter()
router1.register(r'newusers', signup_views.NewUserView, 'newuser')

router2 = routers.DefaultRouter()
router2.register(r'users', login_views.UserView, 'user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('signup/', include(router1.urls)),
    path('login/', include(router2.urls)),
]
