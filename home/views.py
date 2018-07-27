from .models import Question ,post
from django.shortcuts import render, redirect,HttpResponseRedirect ,get_object_or_404
from.forms import postform
from django.utils import timezone
from .forms import UserRegistrationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.generic import RedirectView
from django.http import HttpResponse

def index(request):
    all_questions = Question.objects.all()
    context = {
        'all_questions': all_questions,
    }
    return render(request,'home/index.html',context)

def detail(request,question_id):
    if request.method == "POST":
        form = postform(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.written_by = request.user
            post.image = request.FILES['image']
            post.published_time = timezone.now()
            post.save()
            return redirect('view_post')
    else:
        form = postform()
    return render(request, 'home/index1.html', {'form': form})

def view_post(request ):
    all_posts = post.objects.filter()
    context = {
        'all_posts': all_posts
    }
    return render(request, 'home/index2.html', context)


def home(request):
    return render(request, 'home/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/question/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')

    else:
        form = UserRegistrationForm()

    return render(request, 'home/register.html', {'form' : form})

def profile(request):
    all_posts = post.objects.filter(written_by = request.user)
    context = {
        'all_posts': all_posts
    }
    return render(request, 'home/index3.html', context)


