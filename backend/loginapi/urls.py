from django.urls import path
from loginapi import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('api/login', views.loginapi_list),
    path('api/login/<int:pk>/', views.loginapi_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)