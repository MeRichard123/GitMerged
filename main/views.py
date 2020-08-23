from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.contrib import messages

from .decorators import unauthenticated_user
from users.models import Profile
from .filters import UserFilter

# Create your views here.


@unauthenticated_user
def home(req):
    return render(req, "home.html")


@login_required
def datePage(req):
    users = Profile.objects.all()
    user = req.user

    myFilter = UserFilter(req.GET, queryset=users)
    users = myFilter.qs

    context = {
        'users': users,
        'userIn': user,
        'filter': myFilter
    }
    return render(req, "date-page.html", context)


def likePost(req, pk):
    user = get_object_or_404(Profile, id=req.POST.get("user_id"))

    if req.user in user.likeability.all():
        user.likeability.remove(req.user)
    else:
        user.likeability.add(req.user)
        if user.user in req.user.profile.likeability.all():
            messages.success(req, f"Thats a match, {user.full_name} likes you back!")
    return redirect("home-page")


def blockUser(req, pk):
    user = get_object_or_404(Profile, id=req.POST.get("user_id"))

    if req.user not in user.blocked_by.all():
        user.blocked_by.add(req.user)

    return redirect("home-page")


class UserDetail(DetailView):
    model = Profile
