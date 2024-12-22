from django.contrib import admin
from django.urls import path
from home.views import *
from resume.views import *

urlpatterns = [
    path('' , home_page, name='home_page'),
    path('home-page' , home_page, name='home_page'),
    path('success-page', success_page, name='success_page'),
    path('resume', resumes, name='resume'),
    path('delete-resume/<id>/', delete_resume, name='delete_resume'),
    path('update-resume/<id>/', update_resume, name='update_resume'),
    
    path('contact-page', contact_page, name='contact_page'),
    path('logout-page', logout_page, name='logout_page'), 

    path('login', login_page, name = 'login_page'),

    path('logout-page', logout_page, name='logout-page'),

    path('register', register_page, name = 'register_page'),

    path('admin/', admin.site.urls)
]
