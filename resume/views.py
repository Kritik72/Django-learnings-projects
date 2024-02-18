from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def resumes(request):

    if request.method == 'POST':
        data = request.POST

        f_name = data.get('f_name') 
        l_name = data.get('l_name')
        desc = data.get('desc')
        image = request.FILES.get('image')

        Resume.objects.create(f_name = f_name , 
                              l_name = l_name, 
                              desc = desc,
                              image = image,
                              )
        
        return redirect('/resume')
        
        
    queryset = Resume.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(f_name__icontains = request.GET.get('search'))

    context = {'resume' : queryset}

    return render(request, 'resume.html',context)

def delete_resume(request,id):
    queryset = Resume.objects.get(id = id)

    queryset.delete()  
    return redirect('resume')

def update_resume(request,id):
    queryset = Resume.objects.get(id = id)

    if request.method == 'POST':
        data = request.POST

        f_name = data.get('f_name') 
        l_name = data.get('l_name')
        desc = data.get('desc') 
        image = request.FILES.get('image')

        queryset.f_name = f_name
        queryset.l_name = l_name
        queryset.desc = desc

        if image:
            queryset.image = image

        queryset.save()
        return redirect('/resume')
        
    context = {'resume': queryset}  
    return render(request, 'update.html',context)



def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.info(request, "Invalid Username Or user does not exists.")
            return render(request, 'login.html')
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, "Invalid Password")
            return render(request, 'login.html')
        
        else:
            login(request, user)
            # return render(request, 'resume.html')
            return redirect('resume')
    

    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return render(request, 'login.html')


def register_page(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, "Username already taken.")
            return render(request, 'register.html')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )

        user.set_password(password)
        user.save()

        messages.info(request, "Account created Successfully")

        return render(request, 'register.html')

    return render(request, 'register.html')