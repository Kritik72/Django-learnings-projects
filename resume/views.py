from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse


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
    context = {'resume' : queryset}

    return render(request, 'resume.html', context)

def delete_resume(request,id):
    queryset = Resume.objects.get(id = id)

    queryset.delete()   
    return render('/resume')

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
