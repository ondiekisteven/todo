from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import User


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created successfully. You can now log in')
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def user_redirect(request):
    if request.user.username == '':
        return render(request, 'todo/about.html')
    username = request.user.username
    url = 'user/' + username + '/'
    return redirect(url)


@login_required
def profile(request):
    return render(request, 'users/profile.html')
