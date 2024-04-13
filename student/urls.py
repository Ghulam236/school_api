from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import register_student, login_student, update_student_profile,home,login_view,register_view,update_view



 

urlpatterns = [
    path('home', home, name="home"),
    path('login_view', login_view, name="login_view"),
    path('register_view', register_view, name="register_view"),
    path('update_view', update_view, name="update_view"),

    path('register', register_student, name='register_student'),
    path('login/', login_student, name='login_student'),
    path('update-profile/', update_student_profile, name='update_profile'),
]
    
