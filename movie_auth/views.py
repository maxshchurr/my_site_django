from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import RegistrationForm, LoginForm
from . models import Site_User



def sign_up(request):
    ctx = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():

            cleaned_data = form.cleaned_data
            username = cleaned_data['username']
            password = cleaned_data['password']
            email = cleaned_data['email']
            dob = cleaned_data['dob']

            new_user = Site_User(
                            username=username,
                            email=email,
                            dob=dob
                        )
            new_user.set_password(password)
            new_user.save()

            login(request, new_user)
            return HttpResponse("Success!Signed up")
        else:
            ctx['registration_form'] = form
    else:
        form = RegistrationForm()
        ctx['registration_form'] = form
    return render(request, 'movie_auth/sign_up.html', ctx)



def log_in(request):
    ctx = {}
    user = request.user
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return HttpResponse(f"Success!Logged in")
    else:
        form = LoginForm()
    ctx['login_form'] = form
    return render(request, 'movie_auth/log_in.html', ctx)


def logout_from(request):
    logout(request)
    return HttpResponse("You have logged out from the site")
