import imp
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from .forms import UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model


User = get_user_model()

def Register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        if User.objects.filter(email=email):
            messages.warning(request, "Cet email existe déjà")
            return redirect('register')
        else:
            user = User.objects.create_user(email, phone, password)
            user.last_name = last_name
            user.first_name = first_name
            user.save()
            if user:
                auth = authenticate(username=user.email, password=password)
                if auth is not None:
                    login(request, auth)
                    messages.success(request, "Enregistrement réussit")
                    return redirect('home')
    return render(request, 'accounts/register.html', {})


def Login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if request.method=='POST':
        if(User.objects.filter(email=email).exists()):
            user = authenticate(username=email, password=password)
        else:
            messages.error(request, "Données incorrects! Réessayez")
            return redirect('login')
        if user is not None:
            login(request, user)
            messages.success(request, "Vous êtes connecté")
            return redirect('home')
        else:
            messages.error(request, "Données incorrects! Réessayez")
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def Logout(request):
    logout(request)
    return redirect('login')


@login_required
def Profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    context = { 
        'user': user,
        }
    return render(request, 'accounts/profile.html', context)


@login_required
def UpdateProfile(request, pk):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile', args=[pk]))
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'accounts/update_profile.html', {'form': form})
    