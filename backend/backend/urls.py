from django.contrib import admin
from django.urls import path, include
from todo import views
from rest_framework import routers
from signup import views as signup_views
from login import views as login_views

from django.contrib.auth import views as auth_views

from users import views as user_views

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
    # path('login/', include(router2.urls)),
    path('', login_views.front, name='front'),

    path('register/', user_views.register, name='register'),

    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
