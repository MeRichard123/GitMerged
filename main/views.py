from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView, DeleteView, ListView
from django.contrib import messages

from .decorators import unauthenticated_user
from users.models import Profile, User
from .models import Message
from .filters import UserFilter

# Create your views here.


@unauthenticated_user
def home(req):
    return render(req, "home.html")


@login_required
def datePage(req):
    users = Profile.objects.all()
    user = req.user
    unreadMessages = Message.objects.filter(
        receiver=user).filter(status=False).count()

    myFilter = UserFilter(req.GET, queryset=users)
    users = myFilter.qs

    context = {
        'users': users,
        'userIn': user,
        'filter': myFilter,
        'unreadmsgs': unreadMessages
    }
    return render(req, "date-page.html", context)


@login_required
def likePost(req, pk):
    user = get_object_or_404(Profile, id=req.POST.get("user_id"))

    if req.user in user.likeability.all():
        user.likeability.remove(req.user)
    else:
        user.likeability.add(req.user)
        if user.user in req.user.profile.likeability.all():
            messages.success(
                req, f"Thats a match, {user.full_name} likes you back!")
    return redirect("home-page")


@login_required
def blockUser(req, pk):
    user = get_object_or_404(Profile, id=req.POST.get("user_id"))

    if req.user not in user.blocked_by.all():
        user.blocked_by.add(req.user)

    return redirect("home-page")


class UserDetail(LoginRequiredMixin, DetailView):
    model = Profile


class WriteMessage(LoginRequiredMixin, CreateView):
    model = Message
    fields = ["content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        pk = self.kwargs.get("username")
        form.instance.receiver = User.objects.get(username=pk)
        return super().form_valid(form)


class DeleteMessage(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = "/"


@login_required
def ViewMessages(req):
    messages = Message.objects.filter(receiver=req.user)
    unreadMessages = Message.objects.filter(
        receiver=req.user).filter(status=False).count()
    userIn = req.user

    context = {
        'msgs': messages,
        'userIn': userIn,
        'unreadmsgs': unreadMessages
    }

    return render(req, "messages.html", context)


@login_required
def MarkAsRead(req, pk):
    msg_id = req.POST.get("msg_id")
    message = Message.objects.get(pk=req.POST.get("msg_id"))

    message.status = True
    message.save()

    return redirect("view-messages")
