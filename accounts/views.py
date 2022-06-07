from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import signupform, Profile, Profile_edit_one, Profile_edit_tow
from django.contrib.auth import authenticate, login
from .models import Profile

# Create your views here.

# signup-------------------------


def signup(requset):
    if requset.method == "POST":
        form = signupform(requset.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(requset, user)
        return redirect("/accounts/profile")
    else:
        form = signupform()
    return render(requset, "registration/signup.html", {'form': form})

# profile-------------------------

def profile(requset):
    My_profile = Profile.objects.get(user=requset.user)
    return render(requset, "profile/profile.html", {'My_profile': My_profile})

# profile_edit-------------------------

def profile_edit(requset):
    profile = Profile.objects.get(user=requset.user)
    if requset.method == "POST":
        profile_edit_one = Profile_edit_one(
            requset.POST, instance=requset.user)
        profile_edit_tow = Profile_edit_tow(
            requset.POST, requset.FILES, instance=profile)
        if profile_edit_one.is_valid() and profile_edit_tow.is_valid():
            profile_edit_one.save()
            profile_edit_tow.save(commit=False)
            profile_edit_tow.user = requset.user
            profile_edit_tow.save
            return redirect(reverse("accounts:profile"))
    else:
        profile_edit_one = Profile_edit_one(instance=requset.user)
        profile_edit_tow = Profile_edit_tow(instance=profile)
    return render(requset, "profile/profile_edit.html", {'profile_edit_one': profile_edit_one, 'profile_edit_tow': profile_edit_tow})
