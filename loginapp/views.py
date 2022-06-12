from unicodedata import category
from django.shortcuts import render, redirect

# from login.settings import LOGIN_REDIRECT_URL
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from loginapp.models import blog_data2


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

@login_required(login_url='login_view')
def blogdetails(request):
    if request.method=='POST':
        print('This is post')
        userName=request.POST['userName']
        title=request.POST['title']
        category=request.POST['Category']
        summary=request.POST['summary']
        content=request.POST['content']
        status=request.POST['status']
        ins1=blog_data2(userName=userName,title=title,category=category,summary=summary,content=content,status=status)
        ins1.save()
        print('data stored')
        return redirect('/blog')

    return render(request,'blogdetails.html')

@login_required(login_url='login_view')
def blog(request): 


    allblogs = blog_data2.objects.all()

    context={'allblogs': allblogs}
    return render(request, "blog.html", context)

@login_required(login_url='login_view')
def patient_blog(request):
    allment_health=blog_data2.objects.filter(category='Mental Health',status='Published').all()
    allcovid=blog_data2.objects.filter(category='Covid19',status='Published').all()
    allheart=blog_data2.objects.filter(category='Heart Diease',status='Published').all()
    allimm=blog_data2.objects.filter(category='Immunization',status='Published').all()




    context={'allment_health': allment_health,'allcovid':allcovid,'allheart':allheart,'allimm':allimm}
    return render(request, "patient_blog.html",context)