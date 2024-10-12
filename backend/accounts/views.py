# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm

# register_view(request):
#    if request.method == 'POST':
#        form = CustomUserCreationForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('login')  # Redirigir al login después de registrarse
#    else:
#        form = CustomUserCreationForm()
#    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Cambia 'home' por la vista a la que deseas redirigir
    else:
        form = CustomAuthenticationForm()

    return render(request, 'login.html', {'form': form})

@login_required
def home_view(request):
    return render(request, 'accounts/home.html')  # Crea una plantilla home.html
