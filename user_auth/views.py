from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from .models import User
from django.contrib.auth.models import User

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Use create_user method to create and save the user
            User.objects.create_user(username=form.cleaned_data['username'],
                                     password=form.cleaned_data['password'],
                                     first_name=form.cleaned_data['first_name'])
            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('polls:index')  # Redirect to the polls app after successful login
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')


# Create your views here.