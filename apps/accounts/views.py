from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render

from .forms import ProfileForm
from .models import Profile


def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard:dashboard")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            messages.success(
                request,
                f"Welcome back, {user.username}!"
            )

            return redirect("dashboard:dashboard")
    else:
        form = AuthenticationForm()

    return render(
        request,
        "accounts/login.html",
        {"form": form}
    )


def register_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard:dashboard")

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            Profile.objects.get_or_create(user=user)

            login(request, user)

            messages.success(
                request,
                "Account created successfully!"
            )

            return redirect("dashboard:dashboard")
    else:
        form = UserCreationForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form}
    )


@login_required
def logout_view(request):
    if request.method == "POST":
        logout(request)

        messages.info(
            request,
            "You have been logged out."
        )

        return redirect("accounts:login")

    return render(
        request,
        "accounts/logout_confirm.html"
    )


@login_required
def profile_view(request):
    profile, _ = Profile.objects.get_or_create(
        user=request.user
    )

    return render(
        request,
        "accounts/profile.html",
        {"profile": profile}
    )


@login_required
def profile_edit_view(request):
    profile, _ = Profile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Profile updated successfully!"
            )

            return redirect("accounts:profile")
    else:
        form = ProfileForm(instance=profile)

    return render(
        request,
        "accounts/profile_edit.html",
        {"form": form}
    )