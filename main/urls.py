from django.contrib import admin
from django.urls import path
from . import views
from users import views as user_views

urlpatterns = [
    path('', views.home, name="home-page"),
    path("home/", views.datePage, name="date-page"),
    path("profile/", user_views.profile, name="profile-page"),
    path("like/<int:pk>/", views.likePost, name="like"),
    path("user/<int:pk>/", views.UserDetail.as_view(), name="user-detail"),
    path("block/<int:pk>/", views.blockUser, name="block"),
    path("new-message/<str:username>",
         views.WriteMessage.as_view(), name="write-message"),
    path("view-messages/", views.ViewMessages, name="view-messages"),
    path("mark-read/<int:pk>", views.MarkAsRead, name="mark-read"),
    path("delete/<int:pk>", views.DeleteMessage.as_view(), name="delete-message")
]
