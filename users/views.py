from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm, ProfileUpdateForm
from django.contrib import messages
from django.views.generic import UpdateView, CreateView
from django.contrib.auth.decorators import login_required
from .models import *
from main.models import Message

# Create your views here.


def register(req):
    if req.method == "POST":
        Form = UserRegisterForm(req.POST)
        if Form.is_valid():
            Form.save()
            username = Form.cleaned_data.get("username")
            messages.success(req, f"Account Created. You can now log in")
            return redirect("login")
    else:
        Form = UserRegisterForm()
    return render(req, "users/register.html", {'form': Form})


@login_required
def profile(req):
    user = req.user
    profile = Profile.objects.get(user=user)
    likes = profile.num_likes
    unreadMessages = Message.objects.filter(
        receiver=req.user).filter(status=False).count()
    if req.method == "POST":
        form = ProfileUpdateForm(
            req.POST, req.FILES, instance=req.user.profile)

        if form.is_valid():
            form.save()
            messages.success(req, "Account Updated")
            return redirect("profile-page")
    else:
        form = ProfileUpdateForm(instance=req.user.profile)

    context = {
        'form': form,
        'likes': likes,
        'unreadmsgs': unreadMessages
    }

    return render(req, "users/profile.html", context)
