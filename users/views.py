from django.core.exceptions import ValidationError
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm,RegisterationForm


# Create your views here.
def loginUser(request):
    form=LoginForm(request.POST or None)
    context = {
        'form': form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(request, username=username, password=password)
        if not user:
            raise ValidationError("Invalid Credentials")

        if user is not None:
            login(request, user)
            return redirect('/')
        

    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

User= get_user_model()
def registerUser(request):
    
    form = RegisterationForm(request.POST or None)
    context={
        "form": form
    }
    if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('login')

    return render(request, 'register.html', context)


@login_required(login_url='login')
def posts(request):

    if request.method=='POST':
        user=request.user
        text=request.POST.get('text')
        createdAt=request.POST.get('created_at')
        UpdatedAt=request.POST.get('updated_at')

        data=Post(user=user,text=text,created_at=createdAt,updated_at=UpdatedAt)
        data.save()
        return HttpResponse("sucsessfully posted")
    
        
    
    return render(request,'post.html')