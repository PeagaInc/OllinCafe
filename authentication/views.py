from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from django.contrib.auth.views import LogoutView
from authentication.forms import LoginForm
from core.controller import UserPermissionView
# Create your views here.


def login_view(request):
    form = LoginForm(request.POST or None)
    messages = None
    if request.method == "POST":
        request.session.clear()
        # Clear all session data before login
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                current_user = request.user.pk
                UserPermissionView.get_user(request, current_user)
                if request.session['permission'] == 0:
                    messages = "You do not have access, please contact admin"
                else:
                    return redirect("/")
            else:    
                messages = 'Invalid credentials'    
        else:
            messages = 'Error validating the form'    

    return render(request, "accounts/login.html", {"form": form, "messages" : messages})

