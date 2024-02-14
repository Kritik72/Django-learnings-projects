from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    peoples = [
        {'name' : 'Kritik vaishnav' , 'Age' : 20},
        {'name' : 'Rohan sharma' , 'Age' : 29},
        {'name' : 'Rahul Guptatik' , 'Age' : 12},
        {'name' : 'Abhishek Veeramalla' , 'Age' : 30},
        {'name' : 'Durgesh Classes' , 'Age' : 15}
    ]

    return render(request, 'home\index.html', context = {'peoples':peoples , 
                                                         'page': 'First Django Page'})    

def success_page(request):
    context = {'page' : 'Success'}
    return render(request, 'home\success.html', context)

def contact_page(request):
    context = {'page' : 'Contact'}
    return render(request, 'home\contact.html', context)

def logout_page(request):
    context = {'page': 'About'}
    return render(request, 'home\logout.html', context)
