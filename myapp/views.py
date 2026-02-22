from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile

def signup(request):
    if request.method == 'POST':
        u = request.POST['u']
        e = request.POST['e']
        p = request.POST['p']

        if User.objects.filter(username=u).exists():
            messages.error(request, "Username already exists. Click Login")
            return redirect('signup')

        User.objects.create_user(username=u, email=e, password=p)
        messages.success(request, "Account created. Please login.")
        return redirect('login')

    return render(request, 'signup.html')

def my_login(request):
    if request.method == 'POST':
        u = request.POST['u']
        p = request.POST['p']

        user = authenticate(request, username=u, password=p)

        if user:
            login(request, user)
            return redirect('home')

        messages.error(request, "Invalid credentials.")
        return redirect('login')

    return render(request, 'login.html')


def my_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def index(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def profile(request):
    profile = Profile.objects.filter(user=request.user).first()

    if not profile:
        return redirect('create_profile')

    return render(request, 'profile.html', {'profile': profile})


@login_required(login_url='login')
def create_profile(request):
    if Profile.objects.filter(user=request.user).exists():
        return redirect('profile')

    if request.method == 'POST':
        profile = Profile.objects.create(
            user=request.user,
            name=request.POST['name'],
            age=request.POST['age'],
            contact=request.POST['contact'],
            bio=request.POST['bio']
        )

        if 'image' in request.FILES:
            profile.image = request.FILES['image']
            profile.save()

        return redirect('profile')

    return render(request, 'create_profile.html')


@login_required(login_url='login')
def edit_profile(request):
    profile = Profile.objects.filter(user=request.user).first()

    if not profile:
        return redirect('create_profile')

    if request.method == 'POST':
        profile.name = request.POST['name']
        profile.age = request.POST['age']
        profile.contact = request.POST['contact']
        profile.bio = request.POST['bio']

        if 'image' in request.FILES:
            profile.image = request.FILES['image']

        profile.save()
        return redirect('profile')

    return render(request, 'edit_profile.html', {'profile': profile})
