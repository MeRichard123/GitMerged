from django.contrib import admin
from django.urls import path
from . import views
from users import views as user_views

urlpatterns = [
    path('', views.home, name="home-page"),
    path("home/", views.datePage, name="date-page"),
    path("profile/", user_views.profile, name="profile-page"),
    path("like/<int:pk>", views.likePost, name="like"),
    path("user/<int:pk>", views.UserDetail.as_view(), name="user-detail"),
    path("block/<int:pk>", views.blockUser, name="block")
]
