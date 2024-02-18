from django.shortcuts import render


def home_page(request):
    context = {'page' : 'Index'}
    return render(request, 'home\index.html',context)  
    
def success_page(request):
    context = {'page' : 'Success'}
    return render(request, 'home\success.html', context)

def contact_page(request):
    context = {'page' : 'Contact'}
    return render(request, 'home\contact.html', context)

def logout_page(request):
    context = {'page': 'About'}
    return render(request, 'home\logout.html', context)
