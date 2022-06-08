from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid() :
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form1 = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form1.is_valid():
            username = form1.cleaned_data.get('username')
            password = form1.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None and user.is_doctor:
                login(request, user)
                # print(form1)
                return redirect('doctor')
            elif user is not None and user.is_patient:
                login(request, user)
                return redirect('patient')

            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form1, 'msg': msg})

def logout_view(request):
    logout(request)
    return redirect('login_view')

@login_required(login_url='login_view')
def doctor(request):

    return render(request,'doctor.html')

@login_required(login_url='login_view')
def patient(request):
    return render(request,'patient.html')

