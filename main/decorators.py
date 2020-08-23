from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(req, *args, **kwargs):
        if req.user.is_authenticated:
            return redirect("date-page")
        else:
            return view_func(req, *args, **kwargs)
    return wrapper_func
